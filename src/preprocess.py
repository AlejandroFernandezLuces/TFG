import pandas as pd
from filemanager import FileManager
import numpy as np
import os
import matplotlib.pyplot as plt

path = "/home/alex/Documents/Clase/TFG/Dataset/iskra"

class Preprocess:
    def _process_nan(self, sensor_df):
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

    def _rename_columns(self,sensor_df, sensor_name):
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


    def _fix_time(self,sensor_df):
        """
        Converts the time from string to Datetime, and puts it as the index
        :param sensor_df: the dataframe to transform
        :return:
        """
        sensor_df.Tiempo = pd.to_datetime(sensor_df.Tiempo)
        sensor_df.set_index("Tiempo", inplace=True)
        return  sensor_df

    def _create_dataframes(self,path):
        """
        Takes the CSV files (one for each sensor), converts them to dataframes,
        fixes them so they can be joined, and joins them.
        :return: a list with the dataframes
        """
        sensor_df_list = []
        filenames = os.listdir(path + "/9")
        for filename in filenames:
            #removes the .csv extension
            sensor_name = filename[:-4]
            sensor_df = pd.read_csv(path + "/9/" + filename)
            # drops the unnecessary columns
            sensor_df = sensor_df.drop(columns=["Comment", "Latitude", "Longitude",
                                                "Sonda(m)", "Code"])
            sensor_df = self._fix_time(sensor_df)
            sensor_df = self._process_nan(sensor_df)

            #resamples the df to minute frequency
            sensor_df = sensor_df.resample("Min").mean()
            sensor_df = self._rename_columns(sensor_df, sensor_name)
            sensor_df_list.append(sensor_df)

    def _join_dataframes(self,sensor_df_list):
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

    def get_dataframe(self, path):
        """
        Given a path to a folder with the sensor CSV inside, it returns a
        dataframe with fixed NaNs and all sensors joined in one df.
        :param path: path to a folder with the sensor csv inside.
        :return: Dataframe with all sensors.
        """
        dataframe_list = self._create_dataframes(path)
        return  self._join_dataframes(dataframe_list)


df = Preprocess()
df = df.get_dataframe(path)