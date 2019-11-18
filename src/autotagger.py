import os
import pandas as pd
saving_path = "/home/alex/Documents/Clase/TFG/Dataset/csv_files_tagged/"

filenames = os.listdir(saving_path)

Y = []
x = []
for filename in filenames:
    dataframe = pd.read_csv(saving_path + filename)
    if filename[-5] == "1":
        Y.append(dataframe)
    elif filename[-5] == "0":
        x.append(dataframe)