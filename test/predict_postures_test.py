import os
#import unittest
import requests
#from unittest import TestCase
#from src.app import app
# import src.v1.end_points.predict_postures

#class PredictPostureTest(TestCase):

def setUp():
    #self.app = app.test_client()
    #app.config['TESTING'] = True
    valid_payload = {
        "X0": 0.353975474110861,
        "Y0": -0.08393742415019606,
        "Z0": -1.9187020150855807,
        "X1": -1.1451346767950084,
        "Y1": 1.1585597358089952,
        "Z1": -0.3009517362486465,
        "X2": 0.0866532474465282,
        "Y2": -1.3792006890526534,
        "Z2": -1.2562441192442861,
        "X3": 0.3362995291865317,
        "Y3": -0.6066620805007832,
        "Z3": -1.599962613849931,
        "X4": 0.14195117232024884,
        "Y4": 1.3752045816570326,
        "Z4": -0.17939028352606337,
        "X5": -1.7899510637312714,
        "Y5": 1.1459738004271993,
        "Z5": 0.09593918182005239,
        "X6": 0.5360111806331871,
        "Y6": 0.37871200157816626,
        "Z6": 0.9214466280991446,
        "X7": -2.1124483925408204,
        "Y7": 0.2840568024787469,
        "Z7": 0.810565483509128,
        "X8": -1.2078088839967749,
        "Y8": 0.5881291135062222,
        "Z8": 1.4450981701390642,
        "X9": 0.8783819667072302,
        "Y9": 0.31961277878462285,
        "Z9": 0.01590360530017835,
        "X10": 1.116238484553511,
        "Y10": 2.810264310809873,
        "Z10": -0.9835267460757017,
        "X11": -0.009044094550495718,
        "Y11": 0.007751915931737572,
        "Z11": 0.010268551214031783
    }
    return valid_payload

def test_predict_posture_test(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'predict-posture', 'test')
    #endpoint = 'http://api/v1/predict-posture/test'
    response = requests.get(endpoint)
    #print(response)
    assert response.status_code == 200
    json = response.json()
    assert 'msg' in json
    assert json['msg'] == "Test Endpoint for predict_posture"


def test_predict_posture_predict_class(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'predict-posture', 'predict-class')
    #endpoint = 'http://api/v1/predict-posture/predict-class'
    payload = setUp()
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 200
    json = response.json()
    assert 'class' in json
    assert 'name' in json
    assert 'probability_score' in json
    assert json['class'] == 5
    assert json['class_name'] == 'grab'
    assert json['class'] == 5


def test_predict_posture_predict_class_probability(api_v1_host):
    endpoint = os.path.join(api_v1_host, 'predict-posture', 'predict-probability')
    #endpoint = 'http://api/v1/predict-posture/predict-probability'
    payload = setUp()
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 200
    json = response.json()
    assert len(json) == 5
# End
