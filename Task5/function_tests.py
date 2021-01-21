"""
Module with tests for utils functions.

"""
from source.utils import transform_to_vector, features_validation

#normal dict
test_dict1 = {
    "age": 40, "month": "mar", 
    "job": "student", "nr.employed": 5000
    }

#incorrect format of age
test_dict2 = {
    "age": "twenty", "month": "mar", 
    "job": "student", "nr.employed": 5000
    }

#missed value for "nr.employed"
test_dict3 = {
    "age": 40, "month": "mar", 
    "job": "student"
    }

#nonexistent categorical value
test_dict4 = {
    "age": 40, "month": "EXTRA_MONTH", 
    "job": "student", "nr.employed": 5000
    }


def test_validation():
    assert features_validation(test_dict1) == 200
    assert features_validation(test_dict2) == 402
    assert features_validation(test_dict3) == 401
    assert features_validation(test_dict4) == 402


def test_transform():
    features = transform_to_vector(test_dict1)
    assert len(features) == 1
    assert len(features[0]) == 4
    for feature in features[0]:
        assert type(feature) in [int, float]
    
    