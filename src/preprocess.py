import pandas as pd
from filemanager import FileManager
import numpy as np
import os
import matplotlib.pyplot as plt

path = "/home/alex/Documents/Clase/TFG/Dataset/iskra"
FileManager(path).get_all_csv()

filenames = os.listdir(path + "/9")

sensor_df_list = []
pandas_dict = {}
rename_dict = {}
for filename in filenames:
    sensor_name = filename[:-4]
    sensor_df = pd.read_csv(path + "/9/" + filename)
    sensor_df = sensor_df.drop(columns=["Comment", "Latitude", "Longitude", "Sonda(m)", "Code"])
    sensor_df.Tiempo = pd.to_datetime(sensor_df.Tiempo)
    sensor_df.set_index("Tiempo", inplace=True)
    sensor_df = sensor_df.replace('---', -1)
    sensor_df = sensor_df.replace('Off', 0)
    sensor_df = sensor_df.replace('On', 1)
    sensor_df = sensor_df.astype(int)
    sensor_df = sensor_df.replace(-1, np.NAN)
    sensor_df = sensor_df.interpolate()  # reconstrue os NAN's, pero e bo mirar un analisis mellor
    sensor_df = sensor_df.resample("Min").mean()
    columns = sensor_df.columns
    for elem in sensor_df.columns:
        rename_dict[elem] = elem + sensor_name
    sensor_df = sensor_df.rename(columns=rename_dict)
    sensor_df_list.append(sensor_df)

join = sensor_df_list[0]
for i in range(1, len(sensor_df_list)):
    join = join.join(sensor_df_list[i])

plt.plot(join["Datos1(°)Babor"])
plt.show()