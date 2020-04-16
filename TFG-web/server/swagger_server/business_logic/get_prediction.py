from swagger_server.DAO.towdataDAO import TowdataDAO
from swagger_server.business_logic.pred_alg_selector import PredAlgSelector

#Strategy pattern
class GetPrediction():
    df = TowdataDAO.getData(TowdataDAO)

    def predict_data(self, algorithm):
        prediction = PredAlgSelector.fit_predict(self, self.df, algorithm)
        return prediction

