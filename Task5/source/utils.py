"""
Module with functions for validation and
transformation of dict with features.

"""
from datetime import datetime

from .features_config import cat_features, cont_features
from .features_config import cat_labels_dict, check_types_dict


def features_validation(feature_vector: dict) -> int :
    """
    Returns status code correspondly to features list
    
    Parameters
    ----------
    feature_vector : dict
        DESCRIPTION: loaded json with features
        
    Returns
    -------
    401: if some features are missed
    402: if some features have incorrect format
    200: if features are OK

    """
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S") 
    print('{} | INFO | "features_validation" function was called'.format(time))
    
    for feature in cat_features + cont_features:
        if feature not in feature_vector.keys():
            return 401
        if type(feature_vector[feature]) not in check_types_dict[feature]:
            return 402
    
    #checking existence of categorical values in cat_labels_dict  
    for feature in cat_features:
        cat_value = feature_vector[feature]
        if cat_value not in cat_labels_dict[feature].keys():
            return 402
    
    return 200


def transform_to_vector(feature_vector: dict) -> list :
    """
    Transforms dict with features to 2d-list with encoded 
    categorical features and continuous features. 

    Parameters
    ----------
    feature_vector : dict
        DESCRIPTION: dict from loaded json with features

    Returns
    -------
    features: 2d-list
        DESCRIPTION: list with features for RandomForestClassifier

    """
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S") 
    print('{} | INFO | "transform_to_vector" function was called'.format(time))
    
    features = []
    for feature in cat_features:
        value = feature_vector[feature]
        encoded_value = cat_labels_dict[feature][value]
        features.append(encoded_value)

    for feature in cont_features:
        features.append(feature_vector[feature])

    return [features] 