import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder


class RandomForestPretrained():
    def __init__(self, root_to_model: str, roots_to_encoders: str):
        self.model = joblib.load(root_to_model)  # need to test
        self.encoders_types = ['code_gender',
                               'flag_own_car',
                               'flag_own_realty',
                               'name_income_type',
                               'name_education_type',
                               'name_family_status',
                               'name_housing_type',
                               'occupation_type']
        self.encoders = list()
        for type in self.encoders_types:
            self.encoders.append(joblib.load(f'{roots_to_encoders}/encoder_{type}.joblib'))

    def __encode__(self, X: np.array, cat_values: list):
        X = X.reshape(-1, 1)
        # print(X)
        for ind, enc in zip(cat_values, self.encoders):
            print(X[ind].reshape(-1, 1).dtype)
            X[ind] = enc.transform(X[ind].reshape(-1, 1))
        return X.reshape(1, -1)[0]

    def predict(self, X: np.array, cat_values: list[int]):
        if len(X.shape) != 1: #Need to recreate it with normal exceptions
            print("Wrong data type")
            return None
        X = self.__encode__(X, cat_values)
        return self.model.predict_proba(X.reshape(1, -1))


model = RandomForestPretrained(r'api/random_forest_sklearn_new.joblib', r'api/encoders')