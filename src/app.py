"""  Flask API for Prediction """
import sys, os
from flask import Flask, jsonify

# load modules
import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from src.v1.end_points.predict_postures import blueprint_prediction
from src.v1.end_points.predict_postures import load_models, load_null_value_replacement, load_standered_scaler

API_PATH = os.path.split(os.path.abspath(__file__))[0]
print(API_PATH)
load_models(API_PATH)
load_null_value_replacement(API_PATH)
load_standered_scaler(API_PATH)

# init Flask app
app = Flask(__name__)



# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_prediction, url_prefix="/api/v1/predict-posture")

