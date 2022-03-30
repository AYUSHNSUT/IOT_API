# app.py
import time

import re
import requests
import numpy as np
import sklearn
import pickle as pkl
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)




@app.route('/weather', methods=['GET'])
def respond_weather():
    # Retrieve the arguements from url parameter
    data = request.args.get('exp')
    print(data)
    data=data.split(',')
    data=[float(i) for i in data]
    print(data)
    # Make prediction using model loaded from disk as per the data.
    model = pkl.load(open('model.pkl','rb'))
    prediction = model.predict([data])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)
    
@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    print(data)
    data=data['exp']
    data=data.split(',')
    data=[float(i) for i in data]
    print(data)
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([data])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
