import joblib
import sklearn
import numpy
import json
class LinearRegression():

    def fit_predict(self, data):
        try:
            data = data.drop(columns=["Tiempo", "Escalas(m)"])
        except:
            data = data.drop(columns=["Tiempo", "Datos1(Fa)"])

        data = data.iloc[-160:]

        data = data.to_numpy()

        data = data.reshape(1, -1)
        results = []

        for elem in [1, 2, 3, 5, 8, 13, 21, 34]:

            model = joblib.load("D:/Alex/Documentos/CLASE/TFG/TFG-proyect/TFG-Research/model_persistence/lr_gap="+str(elem)+".joblib")
            try:
                results.append([elem, model.predict(data)[0]])
            except ValueError:
                print("Failed to predict")

        return results
