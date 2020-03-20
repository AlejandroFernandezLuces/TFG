from swagger_server.DAO.towdataDAO import TowdataDAO


class UpdateData():

    def update(self, csv):
        """
        Saves the retrieved file from the client into the server
        :param csv: A string containing a csv
        :return:
        """
        TowdataDAO.updateData(TowdataDAO, csv)