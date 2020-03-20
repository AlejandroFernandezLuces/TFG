from swagger_server.DAO.towdataDAO import TowdataDAO


class DeleteData():

    def delete(self):
        """
        Saves the retrieved file from the client into the server
        :param csv: A string containing a csv
        :return:
        """

        TowdataDAO.deleteData(TowdataDAO)