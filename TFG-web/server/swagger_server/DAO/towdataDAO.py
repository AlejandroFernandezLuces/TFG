import pandas


class TowdataDAO():
    savepath = "D:/Alex/Documentos/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/database/savefile.csv"


    def getData(self):
        try:
            data = pandas.read_csv(self.savepath)
            return data
        except:
            print("The savefile you are trying to reach does not exist or has bad format")

    def saveData(self, csv):
        text_file = open(self.savepath, "w", newline="")
        text_file.write(csv)
        text_file.close()

    def updateData(self, csv):
        postString = csv.split("\n")
        data_headless = "\n"
        for i in range(1, len(postString) - 1):
            data_headless += postString[i] + "\n"
        data_headless += postString[i + 1]
        text_file = open(self.savepath, "a+",  newline="")
        text_file.write(data_headless)
        text_file.close()

    def deleteData(self):
        text_file = open(self.savepath, "r+")
        text_file.seek(0)
        text_file.truncate()
        text_file.close()