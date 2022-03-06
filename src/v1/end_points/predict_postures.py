from flask import Blueprint, jsonify, request
from src.v1 import *
from src.v1.service.prediction_service import PredictService
from src.v1.utils.traindatastats import get_null_replaement_value, get_standered_transformation_object
from src.v1.utils.validation import vaidate_axis_data

blueprint_prediction = Blueprint(name="predict_posture", import_name=__name__)

##################### Load Constants #########################################
prediction_service: PredictService = None
null_replaement_value: Dict[str, float] = None
standered_scaler: object = None

def  load_models(apipath: str)->None:
    global prediction_service

    svmpath =  os.path.join(apipath, 'v1', 'models', '1.0', 'grid_cv_result_svm.pkl')
    dtpath =  os.path.join(apipath, 'v1', 'models', '1.0', 'grid_cv_result_dt.pkl')
    rfpath =  os.path.join(apipath, 'v1', 'models', '1.0', 'grid_cv_result_rf.pkl')
    nnpath =  os.path.join(apipath, 'v1', 'models', '1.0', 'deep_learning_model')
    final_model_path =  os.path.join(apipath, 'v1', 'models', '1.0', 'final_ensamble_model')
    base_model = {
        ModelType.SVM : svmpath,
        ModelType.DECISION_TREE: dtpath,
        ModelType.RANDOM_FOREST : rfpath,
        ModelType.DNN : nnpath
    }
    prediction_service = PredictService(base_model, final_model_path)
# End


def load_null_value_replacement(apipath: str)->None:
    global null_replaement_value
    file_path =  os.path.join(apipath, 'v1', 'resources', 'null_replacement_value.json')
    null_replaement_value = get_null_replaement_value(file_path)
# End


def load_standered_scaler(apipath: str)->None:
    global standered_scaler
    file_path =  os.path.join(apipath, 'v1', 'resources', 'standered_scaler_object.pkl')
    standered_scaler = get_standered_transformation_object(file_path)
# End

@blueprint_prediction.route('/', methods=['GET'])
def test():
    try:
        output = {"msg": "Test Endpoint for predict_posture"}
        return jsonify(output), 200
    except Exception as e:
        return jsonify({'error' : e})
# End

@blueprint_prediction.route('/class-mapping', methods=['GET'])
def class_mapping():
    try:
        mapping = prediction_service.class_mapping
        return jsonify(mapping), 200
    except Exception as e:
        return jsonify({'error' : e}), 500
# End


@blueprint_prediction.route('/predict-class', methods=['POST'])
def predict_class():
    try:
        # retrieve body data from request body
        data = request.get_json()
        axis_np = vaidate_axis_data(data, null_replaement_value)
        std_data = standered_scaler.transform(axis_np.reshape(1, -1))
        # compute result
        label, prob, name = prediction_service.predict(std_data.reshape(-1))
        output = {"class": int(label), "probability_score": float(prob), 'class_name': name}
        return jsonify(output), 200
    except Exception as e:
        return jsonify({'error' : e}), 500
# End


@blueprint_prediction.route('/predict-probability', methods=['POST'])
def predict_class_probability():
    try:
        # retrieve body data from request body
        data = request.get_json()
        axis_np = vaidate_axis_data(data, null_replaement_value)
        std_data = standered_scaler.transform(axis_np.reshape(1, -1))
        # compute result
        prob = prediction_service.predict_probaility(std_data.reshape(-1))
        output = [{'class': key, 'probability' : value } for key, value in prob.items()]
        return jsonify(output), 200
    except Exception as e:
        return jsonify({'error': e}), 500
# End
