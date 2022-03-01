from src.v1 import *

class PredictService:

    def __init__(self, base_model_path: Dict[ModelType, str], final_model_path:  str)->None:
        """
        predict the posture

        parameter
        ----------

        base_model_path: Dict[ModelType, str]

        base model type to path mapping 1st level of predictors are used here 

        final_model_path: str
        
        2nd level model predictor path

        returns
        -------

        None

        """
        self.base_learner: Dict[ModelType, object] = {}

        self.classname = {
            1 : "fist",
            2: "stop",
            3: "point with one finger",
            4 : "point with two fingers",
            5 : "grab"
        }
        for model, path in base_model_path.items():
            if os.path.exists(path):
                if model  == ModelType.DNN:
                    self.base_learner[model] = tf.keras.models.load_model(path)
                else:
                    with open(path, 'rb') as f:
                        self.base_learner[model] = pickle.load(f).best_estimator_
                    
            # End
        # End

        self.final_model = None

        if not os.path.exists(final_model_path):
            raise FileExistsError("Provided path {0} does not exists".format(final_model_path))
        
        self.final_model = tf.keras.models.load_model(final_model_path)

     # End
    

    def _get_model_output(self, data: np.array)-> np.array:        
        """
        return the model output numpy array

        parameter
        ---------

        data: np.array
            data provided as numpy array of dimension 36 (12 X 3 Axis data serially from (X1, Y1, Z1) -> (X12, Y12, Z12))
        
        returns
        ---------

        np.array

            probability
        
        """
        pred_svm = self.base_learner[ModelType.SVM].predict_proba(data.reshape(1, -1))
        pred_dt = self.base_learner[ModelType.DECISION_TREE].predict_proba(data.reshape(1, -1))
        pred_rf = self.base_learner[ModelType.RANDOM_FOREST].predict_proba(data.reshape(1, -1))
        pred_nn = self.base_learner[ModelType.DNN].predict(data.reshape(1, -1))

        X_ens = np.concatenate([pred_rf, pred_dt, pred_svm, pred_nn], axis=1)
        y_pred = self.final_model.predict(X_ens)
        return y_pred
    # End

    
    def predict_probaility(self, data: np.array) -> Dict[str, float]:
        """
        predict probability of the class

        parameter
        -----------

        data: np.array

            data provided as numpy array of dimension 36 (12 X 3 Axis data serially from (X1, Y1, Z1) -> (X12, Y12, Z12))
        
        returns
        -----------

        numpy array
            
            probability output of Dictionary [class label to probability mapping]

        """
        y_prob = self._get_model_output(data)
        res = dict(zip(self.classname.values(), y_prob[0].astype(float)))
        return res
    # End


    def predict(self, data: np.array) -> np.array:
        """
        predict class label encoding of the class

        parameter
        -----------

        data: np.array

            data provided as numpy array of dimension 36 (12 X 3 Axis data serially from (X1, Y1, Z1) -> (X12, Y12, Z12))
        
        returns
        -----------

        numpy array
            
            class label encoded value

        """
        y_prob = self._get_model_output(data)[0]
        max_idx = np.argmax(y_prob)
        return max_idx + 1 , y_prob[max_idx], self.classname[max_idx+1] # +1 since class label started from 1 not from 0
    # End
# End


        


