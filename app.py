# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

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
    return input_values


# for single value

@app.route("/", methods=['GET','POST'])
def homepage():
    if(request.method=="POST"):
        output = predict(request.form["height"], request.form["radius"], request.form["freq"])
        return render_template("index.html", result=output)

    return render_template("index.html")


# for range values

@app.route("/range", methods=['GET','POST'])
def range_input():
    if(request.method=="POST"):
        height = np.arange(request.form["height_start"], request.form["height_stop"]+request.form["height_step"], request.form["height_step"])
        radius = np.arange(request.form["radius_start"], request.form["radius_stop"]+request.form["radius_step"], request.form["radius_step"])
        freq = np.arange(request.form["freq_start"], request.form["freq_stop"]+request.form["freq_step"], request.form["freq_step"])

        predict_range(height, radius, freq)
        return render_template("range_input.html", result=1.2)

    return render_template("range_input.html")

if __name__ == '__main__':
    app.run(debug=True)
