import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy import signal
import towfileseparator
import dataframemanager

path = "/home/alex/Documents/Clase/TFG/Dataset/iskra/"
saving_path =  "/home/alex/Documents/Clase/TFG/Dataset/csv_files/"

dataframemanager._create_dataframes(path + "9/")

"""
towfileseparator.separate_tows(path, saving_path)

filenames = os.listdir(saving_path)


dataframe = pd.read_csv(saving_path + filenames[11])
apertura = dataframe["Datos2(m)Estribor"]
apertura_suavizado = signal.savgol_filter(apertura, 53, 3)
"""