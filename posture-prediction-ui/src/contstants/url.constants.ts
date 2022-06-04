import {environment} from '../environments/environment';

export  class URLConstant {

    public static PREDICT_TEST_URL = environment.baseUrl + 'api/v1/predict-posture';
    public static CLASS_MAPPING_URL = environment.baseUrl + 'api/v1/predict-posture/class-mapping';
    public static PREDICT_PROBABILITY_URL = environment.baseUrl + 'api/v1/predict-posture/predict-probability';
    public static PREDICT_CLASS_LABEL_URL =  environment.baseUrl + 'api/v1/predict-posture/predict-class';
}
