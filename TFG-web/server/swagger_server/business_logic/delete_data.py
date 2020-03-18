class DeleteData():
    savepath = "C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/database/savefile.csv"

    def delete(self):
        """
        Saves the retrieved file from the client into the server
        :param csv: A string containing a csv
        :return:
        """

        text_file = open(self.savepath, "r+")
        text_file.seek(0)
        text_file.truncate()
        text_file.close()