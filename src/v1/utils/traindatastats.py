import json
from typing import Dict
from src.v1 import pickle

def get_null_replaement_value(axis_mapping_filepath: str)->Dict[str, float]:
    """
    return the value used to replace if null or no value present in axis data

    parameter
    ---------

    axis_mapping_filepath: str

        json file path where axis null value replacement value stored

    """
    data = None
    with open(axis_mapping_filepath, 'r') as f:
        data = json.load(f)
    return data
# End


def get_standered_transformation_object(filepath: str)->object:
    """
    return the standered scaler object to standerized the data fitted on train data

    parameter
    ----------

    filepath: str

        filepath where standered scaler pickle object present

    returns
    ----------

        standered scaler object

    """
    obj = None
    with open(filepath, 'rb') as f:
        obj = pickle.load(f)
    return obj
# End
