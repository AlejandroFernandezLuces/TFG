from swagger_server.DAO.towdataDAO import TowdataDAO
from swagger_server.business_logic.pred_alg_selector import PredAlgSelector

#Strategy pattern
class GetPrediction:

    def predict_data(self, algorithm):
        df = TowdataDAO.getData(TowdataDAO)
        prediction = PredAlgSelector.fit_predict(self, df, algorithm)
        return prediction

