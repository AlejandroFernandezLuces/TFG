import pandas as pd
import numpy as np
import os

def _process_nan(sensor_df):
    """
    Transforms the empty values of the df to NaN values, and then
    interpolates them
    :param sensor_df: the dataframe to transform
    :return: the df with the interpolated values
    """
    sensor_df = sensor_df.replace('---', -1)
    sensor_df = sensor_df.replace('Off', 0)
    sensor_df = sensor_df.replace('On', 1)
    sensor_df = sensor_df.astype(int)
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
            # drops the unnecessary columns
            sensor_df = sensor_df.drop(columns=["Comment", "Latitude", "Longitude",
                                                "Sonda(m)", "Code"])
            sensor_df = _fix_time(sensor_df)
            sensor_df = _process_nan(sensor_df)

            #resamples the df to minute frequency
            sensor_df = sensor_df.resample("Min").mean()
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
    join = sensor_df_list[0]
    for i in range(1, len(sensor_df_list)):
        join = join.join(sensor_df_list[i])
    return join

def _fix_time(sensor_df):
    """
    Converts the time from string to Datetime, and puts it as the index
    :param sensor_df: the dataframe to transform
    :return:
    """
    sensor_df.Tiempo = pd.to_datetime(sensor_df.Tiempo)
    sensor_df.set_index("Tiempo", inplace=True)
    return  sensor_df

def     get_dataframe(path):
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

