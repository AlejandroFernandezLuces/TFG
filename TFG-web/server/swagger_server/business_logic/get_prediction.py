from swagger_server.DAO.towdataDAO import TowdataDAO

#Strategy pattern
class GetPrediction():
    df = TowdataDAO.getData()

    def predict_data(self, algorithm):
