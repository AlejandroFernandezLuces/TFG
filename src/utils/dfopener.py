import pandas as pd
import os


def df_opener(path, min_sensor_reads=20):
    directory = os.listdir(path)
    df_list = []
    for file in directory:
        df = pd.read_csv(path + file)
        if df.shape[0] > min_sensor_reads:
            df = df.drop(columns=["Tiempo"])
            df_list.append(df)
    return df_list