from swagger_server.DAO.towdataDAO import TowdataDAO


class SaveData:

    def save(self, csv):
        """
        Saves the retrieved file from the client into the server
        :param csv: A string containing a csv
        :return:
        """
        TowdataDAO.saveData(TowdataDAO, csv)