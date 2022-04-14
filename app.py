# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template, make_response, url_for
import pickle
import os
import pandas as pd


app = Flask(__name__)


# Load the model
model = pickle.load(open('model.pkl', 'rb'))


def predict(height, radius, freq):
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([np.array([height, radius, freq])])

    # Take the first value of prediction
    output = prediction[0]
    return output


def predict_range(height, radius, freq):
    input_values = np.stack(np.meshgrid(height, radius, freq), -1).reshape(-1, 3)
    prediction = model.predict(input_values)
    final_result = np.c_[input_values, prediction]
    return final_result


# for homepage
@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")


# for single value
@app.route("/single", methods=['GET','POST'])
def single():
    if(request.method=="POST"):
        print(request.form)
        output = predict(request.form["height"], request.form["radius"], request.form["freq"])
        return render_template("single_input.html", result=output)

    return render_template("single_input.html")


# for range values
@app.route("/range", methods=['GET','POST'])
def range_input():
    if(request.method=="POST"):
        # generating input combination
        height = np.arange(float(request.form["height_start"]), float(request.form["height_end"])+float(request.form["height_step"]), float(request.form["height_step"]))
        radius = np.arange(float(request.form["radius_start"]), float(request.form["radius_end"])+float(request.form["radius_step"]), float(request.form["radius_step"]))
        freq = np.arange(float(request.form["freq_start"]), float(request.form["freq_end"])+float(request.form["freq_step"]), float(request.form["freq_step"]))

        # predicting result
        output = predict_range(height, radius, freq)

        # generating csv result
        resp = make_response(pd.DataFrame(output, columns=["Height [mm]", "Radius [mm]", "Freq [GHz]", "S11 [dB]"]).to_csv(index=False))
        resp.headers["Content-Disposition"] = "attachment; filename=range_output.csv"
        resp.headers["Content-Type"] = "text/csv"
        return resp

    return render_template("range_input.html")


if __name__ == '__main__':
    app.run(debug=True)
