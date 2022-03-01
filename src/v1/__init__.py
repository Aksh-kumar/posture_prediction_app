import os
import pickle
import numpy as np
import logging
try:
    import tensorflow as tf
    #logging.getLogger("tensorflow").setLevel(logging.ERROR)
except:
    pass
from typing import Dict
from src.v1.utils.modeltype import ModelType