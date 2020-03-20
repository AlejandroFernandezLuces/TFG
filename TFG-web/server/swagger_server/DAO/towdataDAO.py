import pandas


class TowdataDAO():
    savepath = "C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/database/savefile.csv"


    def getData(self):
        data = pandas.read_csv(self.savepath)
        return data

    def saveData(self, csv):
        text_file = open(self.savepath, "w")
        text_file.write(csv)
        text_file.close()

    def updateData(self, csv):
        postString = csv.split("\n")
        data_headless  = ""
        for i in range(1, len(postString) - 1):
            data_headless += postString[i] + "\n"
        data_headless += postString[i + 1]
        print(data_headless)
        text_file = open(self.savepath, "a+")
        text_file.write(data_headless)
        text_file.close()

    def deleteData(self):
        text_file = open(self.savepath, "r+")
        text_file.seek(0)
        text_file.truncate()
        text_file.close()