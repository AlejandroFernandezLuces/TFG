class UpdateData():
    savepath = "C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/database/savefile.csv"

    def update(self, csv):
        """
        Saves the retrieved file from the client into the server
        :param csv: A string containing a csv
        :return:
        """
        postString = csv.split("\n")
        data_headless  = ""
        for i in range(1, len(postString) - 1):
            data_headless += postString[i] + "\n"
        data_headless += postString[i + 1]
        print(data_headless)
        text_file = open(self.savepath, "a+")
        text_file.write(data_headless)
        text_file.close()