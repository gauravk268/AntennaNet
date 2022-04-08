# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

def predict(height, radius, freq):
    prediction = model.predict([np.array([height, radius, freq])])
    output = prediction[0]
    return output

@app.route("/", methods=['GET','POST'])
def homepage():
    if(request.method=="POST"):
        output = predict(request.form["height"], request.form["radius"], request.form["freq"])
        return render_template("index.html", result=output)

    return render_template("index.html")

# @app.route('/api', methods=['POST'])
# def predict():
#     # Get the data from the POST request.
#     data = request.get_json(force=True)

#     # Make prediction using model loaded from disk as per the data.
#     prediction = model.predict([np.array(data['exp'])])

#     # Take the first value of prediction
#     output = prediction[0]

#     return jsonify(output)

# @app.route('/sub', methods=['POST'])
# def submit():
#     if request.method == "POST":
#         name=request.form["username"]

#     return render_template("sub.html", n=name)

if __name__ == '__main__':
    app.run(debug=True)
