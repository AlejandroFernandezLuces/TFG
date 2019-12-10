import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def _process_nan(sensor_df):
    """
    Transforms the empty values of the df to NaN values, and then
    interpolates them
    :param sensor_df: the dataframe to transform
    :return: the df with the interpolated values
    """
    sensor_df = sensor_df.replace('---', -1)
    sensor_df = sensor_df.replace('---.---', -1)
    sensor_df = sensor_df.replace('Off.---', "Off")
    sensor_df = sensor_df.replace('On.---', "On")

    sensor_df = sensor_df.replace('Off', 0)
    sensor_df = sensor_df.replace('On', 1)
    sensor_df = sensor_df.astype(float)

    sensor_df = sensor_df.replace(-1, np.NAN)
    sensor_df = sensor_df.interpolate()  # reconstrue os NAN's, pero e bo mirar un analisis mellor
    return sensor_df

def _rename_columns(sensor_df, sensor_name):
    """
    There is a df for each sensor, and they have the same name on the columns.
    If we want to join the tables (which we want) we need to rename the columns
    so they have the info about what sensor it belongs to
    :param sensor_df: the dataframe to transform
    :return: The df with the right columns
    """
    rename_dict = {}
    for elem in sensor_df.columns:
        rename_dict[elem] = elem + sensor_name
    sensor_df = sensor_df.rename(columns=rename_dict)
    return sensor_df


def _fix_decimals(dataframe):
    """
    It's a must to pass the data before string conversion
    :param dataframe:
    :return:
    """
    columns = dataframe.columns
    dataframe[columns[2]] = dataframe[columns[2]] \
                              + "." \
                              + dataframe[columns[3]]

    dataframe[columns[3]] = dataframe[columns[4]] \
                             + "." \
                             + dataframe[columns[5]]


def _process_df(sensor_df, resample=True):

    columns = sensor_df.columns
    sensor_df = sensor_df.where(sensor_df[columns[2]] != "---")
    sensor_df = sensor_df.drop(columns=["Comment"])
    sensor_df = sensor_df.dropna()
    _fix_decimals(sensor_df)

    # drops the unnecessary columns
    columns = sensor_df.columns
    sensor_df = sensor_df.drop(columns=[columns[0], columns[4],
                                        columns[5], columns[6],
                                        columns[7]])

    sensor_df = _fix_time(sensor_df)
    sensor_df = _process_nan(sensor_df)

    if resample:
        # resamples the df to minute frequency
        sensor_df = sensor_df.resample("4Min").mean()
        sensor_df = _process_nan(sensor_df)  # necesario porque o resample deixa Nans
        """
        #Debugging de graficas antes de cortalas
        plt.clf()
        plt.plot(sensor_df["Escalas(m)"])
        plt.pause(5)
        plt.show()"""
    return sensor_df

def _create_dataframes(path):
    """
    Takes the CSV files (one for each sensor), converts them to dataframes,
    fixes them so they can be joined, and joins them.
    :return: a list with the dataframes
    """
    sensor_df_list = []
    if os.path.isdir(path):
        filenames = os.listdir(path)
        for filename in filenames:
            #removes the .csv extension
            sensor_name = filename[:-4]
            sensor_df = pd.read_csv(path + filename)
            sensor_df =_process_df(sensor_df)
            sensor_df = _rename_columns(sensor_df, sensor_name)
            sensor_df_list.append(sensor_df)

        return sensor_df_list

def _join_dataframes(sensor_df_list):
    """
    Takes a list of dataframes and joins them, being the first of the list
    the leftmost table to join, left joining the rest of the tables.
    :param sensor_df_list: List of dfs
    :return: joined list of dfs in one df
    """
    if len(sensor_df_list) != 0:
        join = sensor_df_list[0]
        for i in range(1, len(sensor_df_list)):
            join = join.join(sensor_df_list[i])
        return join
    else:
        return pd.DataFrame(data=sensor_df_list, columns=[])


def _fix_time(sensor_df):
    """
    Converts the time from string to Datetime, and puts it as the index
    :param sensor_df: the dataframe to transform
    :return:
    """
    sensor_df.Tiempo = pd.to_datetime(sensor_df.Tiempo)
    sensor_df.set_index("Tiempo", inplace=True)
    return  sensor_df

def get_dataframe(path):
    """
    Given a path to a folder with the sensor CSV files inside, it returns a
    dataframe with fixed NaNs and all sensors joined in one df.
    :param path: path to a folder with the sensor csv inside.
    :return: Dataframe with all sensors.
    """
    dataframe_list = _create_dataframes(path)
    if len(dataframe_list) == 0:
        print(path)
    return  _join_dataframes(dataframe_list)

def get_all_dataframes(path):
    """
    Given a path to a folder with several folders inside containing
    CSV files inside, converts them to a list of dataframes. .i.e.

    --- Dataset path
         |
         |--Single Tow 1
         |       |-- Sensor1.csv
         |       |-- Sensor2.csv
         |                 .
         |                 .
         |
         |--Single Tow 2

    :param path: Path to the folder of CSV folders
    :return:
    """
    filenames = os.listdir(path)
    dataframe_list = []
    for filename in filenames:
        if os.path.isdir(path + filename):
            dataframe_list.append(get_dataframe(path + filename + "/"))
    return dataframe_list


def get_aperture_only(path):

    dataframe_list = []
    directory_names = os.listdir(path)
    for directory in directory_names:
        subpath = path + directory + "/"
        if os.path.isdir(subpath):
            filenames = os.listdir(subpath)
            for filename in filenames:
                if (filename == "Abertura.csv") and ("abdera" in directory):
                    df = pd.read_csv(subpath + filename)
                    df = _process_df(df, False)
                    dataframe_list.append(df)
                elif filename == "Estribor.csv":
                    df = pd.read_csv(subpath + filename)
                    df = _process_df(df, False)
                    dataframe_list.append(df)
    return dataframe_list





