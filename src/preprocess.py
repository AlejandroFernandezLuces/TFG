import pandas as pd
from filemanager import FileManager
import numpy as np
import os
path = "/home/alex/Documents/Clase/TFG/Dataset/iskra"
FileManager(path).get_all_csv()

filenames = os.listdir(path + "/9")
sensor_csv_list = []
for filename in filenames:
    sensor_csv = pd.read_csv(path + "/9/" + filename)
    sensor_csv = sensor_csv.drop(columns=["Comment", "Latitude", "Longitude", "Sonda(m)", "Code"])
    sensor_csv.Tiempo = pd.to_datetime(sensor_csv.Tiempo)
    sensor_csv.set_index("Tiempo", inplace=True)
    sensor_csv = sensor_csv.replace('---', -1)
    sensor_csv = sensor_csv.replace('Off', 0)
    sensor_csv = sensor_csv.replace('On', 1)
    sensor_csv = sensor_csv.astype(int)
    sensor_csv = sensor_csv.replace(-1, np.NAN)
    sensor_csv = sensor_csv.interpolate()  # reconstrue os NAN's, pero e bo mirar un analisis mellor
    sensor_csv = sensor_csv.resample("Min").mean()
    sensor_csv_list.append(sensor_csv) #TODO: Pasar esto a dict con code como clave
