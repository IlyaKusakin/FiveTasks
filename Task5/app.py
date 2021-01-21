"""
Main module with Flask application and routes.

"""
import os
import json
import pickle
from datetime import datetime

from flask import Flask
from flask import request
from flask import jsonify

from source.utils import transform_to_vector, features_validation

application = Flask(__name__)
with open(r'models\classifier.pkl', 'rb') as clf:
    classifier = pickle.load(clf)
    clf.close()


@application.route('/hello_world', methods=['GET'])
def hello_world():
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S") 
    print('{} | INFO | "hello_world" route was called'.format(time))
    
    resp = {'result': 'hello_world'}
    response = jsonify(resp)
    return response


@application.route('/calc_proba', methods=['POST'])
def calc_proba():
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S") 
    print('{} | INFO | "calc_proba" route was called'.format(time))
    
    response = {
        'status': None,
        'error_code': None,
        'proba': None
        }

    data = request.get_data()
    features = json.loads(data)
    status = features_validation(features)
    response['status'] = status
    
    if status == 200:
        features = transform_to_vector(features)
        probabilities = classifier.predict_proba(features)[0]
        response['proba'] = probabilities[1]
    if status == 401:
        response['error_code'] = 'incorrect fields'
    if status == 402:
        response['error_code'] = 'incorrect format'

    response = jsonify(response)
    return response


if __name__ == "__main__":

    port = int(os.getenv('PORT', 5000))
    application.run(debug=False, port=port, host='0.0.0.0', threaded=True)