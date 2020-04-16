import joblib

class LinearRegression():

    def fit_predict(self, data):
        data = data.drop(columns=["Tiempo", "Datos1(Fa)"])
        data = data.iloc[-160:]
        data = data.to_numpy()
        data = data.reshape(1, -1)

        results = {}
        for elem in [1, 2, 3, 5, 8, 13, 21, 34]:
            model = joblib.load("C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-Research/model_persistence/lr_gap="+str(elem)+".joblib")
            results[elem] = model.predict(data)[0]
        return results