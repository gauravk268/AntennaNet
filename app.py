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

@app.route("/", methods=['GET','POST'])
def homepage():
    if(request.method=="POST"):
        output = predict(request.form["height"], request.form["radius"], request.form["freq"])
        return render_template("index.html", result=output)

    return render_template("index.html")

@app.route("/range", methods=['GET','POST'])
def range_input():
    if(request.method=="POST"):
        console.log(request.form);
        output = predict(request.form["height"], request.form["radius"], request.form["freq"])
        return render_template("range_input.html", result=output)

    return render_template("range_input.html")

if __name__ == '__main__':
    app.run(debug=True)
