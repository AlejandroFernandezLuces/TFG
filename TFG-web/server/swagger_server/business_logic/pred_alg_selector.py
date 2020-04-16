
from swagger_server.business_logic.ml_models.linear_regression import LinearRegression


class PredAlgSelector():

    def fit_predict(self, data, algorithm):

        if algorithm == "LR":
            prediction = LinearRegression.fit_predict(self, data)
        return prediction