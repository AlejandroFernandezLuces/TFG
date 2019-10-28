import pandas as pd
from filemanager import FileManager
path = "/home/alex/Documents/Clase/TFG/Dataset/iskra"
FileManager(path).get_all_csv()

#Babor = pd.read_csv(path + "/9/Babor.csv")