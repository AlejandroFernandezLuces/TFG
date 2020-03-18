class SaveData():
    savepath = "C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/database/savefile.csv"

    def save(self, csv):
        """
        Saves the retrieved file from the client into the server
        :param csv: A string containing a csv
        :return:
        """

        text_file = open(self.savepath, "w")
        text_file.write(csv)
        text_file.close()