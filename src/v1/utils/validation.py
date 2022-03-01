from src.v1 import np
from typing import Dict

def vaidate_axis_data(data: Dict[str, float], null_replace_value: Dict[str, float])-> np.array:
        """
        validate all the data and replace the data which value is not provided by the value present in null_replace_value

        parameter
        ----------

        data: Dict[str, float] :

            data dictionary mapping from axis name to value
        
        null_replace_value : Dict[str, float]

            replacement value for axis which data is not present
        
        returns
        --------

        all the axis data value as numpy array

        """
        
        mandatory_value = set(['X0', 'Y0', 'Z0', 'X1', 'Y1', 'Z1', 'X2', 'Y2', 'Z2'])
        
        other_axis = ['X3', 'Y3', 'Z3', 'X4', 'Y4', 'Z4', 'X5', 'Y5', 'Z5', 'X6',
                      'Y6', 'Z6', 'X7', 'Y7', 'Z7', 'X8', 'Y8', 'Z8', 'X9', 'Y9',
                      'Z9', 'X10', 'Y10', 'Z10', 'X11', 'Y11', 'Z11']

        present_axis = set(data.keys())

        if len(present_axis.intersection(mandatory_value)) != len(mandatory_value):
            missing_axis = ','.join(x for x in list(mandatory_value - present_axis))
            raise ValueError(f"{missing_axis} these axis values are mandatory")
        
        values = np.array([data[axis] if axis in data else null_replace_value[axis] for axis in list(mandatory_value) + other_axis])

        return values
    # End