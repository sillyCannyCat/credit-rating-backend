import numpy as np
from .model import model
def get_model_predictions(data:dict):
    to_model = list()
    cat_indexes = list()
    cat_features = ['code_gender',
                   'flag_own_car',
                   'flag_own_realty',
                   'name_income_type',
                   'name_education_type',
                   'name_family_status',
                   'name_housing_type',
                   'occupation_type']
    for ind, key in enumerate(data.keys()):
        if key in cat_features:
            cat_indexes.append(ind)
        to_model.append(data[key])
    to_model = np.array(to_model)
    result = True if model.predict(to_model, cat_indexes)[0] == 0 else False
    return {"result":result}