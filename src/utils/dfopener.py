import pandas as pd
import os


def column_selector(df):
    df = df.drop(columns=["Tiempo"])
    print(df.columns)
    try:
        df = df[["Escalas(m)Abertura", "Datos1(m)Abertura"]]
    except:
        try:
            df = df[["Escalas(m)Estribor", "Datos1(Fa)Estribor"]]
        except:
            try:
                df = df[["Escalas(m)", "Datos1(Fa)"]]
            except:
                try:
                    df = df[["Escalas(m)", "Datos1(m)"]]
                except:
                    df = []

    try:
        df = df.dropna()
    except:
        df = []
    return df


def df_opener(path, min_sensor_reads=20):
    directory = os.listdir(path)
    df_list = []
    for i in range(directory.__len__()):
        file = directory[i]
        df = pd.read_csv(path + file)
        if df.shape[0] > min_sensor_reads:
            df = column_selector(df)
            df_list.append(df)
    return df_list