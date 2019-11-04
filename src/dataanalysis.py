from dataframemanager import DataframeManager
import matplotlib.pyplot as plt
import math
import pandas as pd

path = "/home/alex/Documents/Clase/TFG/Dataset/iskra/"

unseparated_df_list = DataframeManager.get_all_dataframes(path)

df_index = 0
for unseparated_df in unseparated_df_list:
    towing_data_only = unseparated_df.where\
        (unseparated_df["Escalas(m)Estribor"] >
         unseparated_df["Escalas(m)Estribor"].mean())

    i = 0
    nonnan_index = []
    while i < len(towing_data_only):
        if not math.isnan(towing_data_only["Escalas(m)Estribor"][i]):
            nonnan_index.append(i)
        i += 1

    end_index = []
    start_index = []
    start_index.append(nonnan_index[0])
    for i in range(1, len(nonnan_index) - 1):
        if nonnan_index[i] + 1 != nonnan_index[i + 1]:
            end_index.append(nonnan_index[i])
        if nonnan_index[i] - 1 != nonnan_index[i - 1]:
            start_index.append(nonnan_index[i])
    end_index.append(nonnan_index[len(nonnan_index) - 1])


    for i in range(len(end_index)):
        df = unseparated_df[start_index[i]:end_index[i]]
        df.to_csv("/home/alex/Documents/Clase/TFG/Dataset/"
                  + str(df_index) + "-" + str(i) + ".csv" )
    df_index += 1
    print(df_index)