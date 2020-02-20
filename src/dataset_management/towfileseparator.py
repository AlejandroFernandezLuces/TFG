from dataset_management import dataframemanager as dfm
import math

"""
Omellor este ficheiro deberia ir dentro de dataframemanager, porque fai 
operacions sobre os dataframes, ainda que sexan lixeiramente diferentes

"""

def select_valid_index(towing_data, full_data=True):
    """
    Selects the indexes where the data is not NaN
    :param towing_data: Dataset
    :return: list with the indexes
    """
    i = 0
    nonnan_index = []
    if full_data:
        column_name = "Escalas(m)Estribor"
    else:
        column_name = "Escalas(m)"
    while i < len(towing_data):
        try:
            if not math.isnan(towing_data[column_name][i]):
                nonnan_index.append(i)
            i += 1
        except:
            i += 1
            continue
    return nonnan_index


def limits_index(towing_data):
    """
    Gives the limits between valid and invalid data in a dataset
    :param nonnan_index: List with the indexes where data is valid
    :return:two lists, one with the start indexes, and one with the end indexes
    """

    nonnan_index = select_valid_index(towing_data, False)
    end_index = []
    start_index = []
    if len(nonnan_index) != 0:
        start_index.append(nonnan_index[0])
        for i in range(1, len(nonnan_index) - 1):
            if nonnan_index[i] + 1 != nonnan_index[i + 1]:
                end_index.append(nonnan_index[i])
            if nonnan_index[i] - 1 != nonnan_index[i - 1]:
                start_index.append(nonnan_index[i])
        end_index.append(nonnan_index[len(nonnan_index) - 1])


    return start_index, end_index


def save_to_csv(path, filename, original_df, start_index, end_index):
    """
    Saves the different tows from one file into one csv each
    :return:
    """
    for i in range(len(end_index) - 1):

        try:
            df = original_df[start_index[i]:end_index[i]]
            if df.__len__() > 0:
                df.to_csv(path + str(filename) + "-" + str(i) + ".csv")
        except:
            print("Start index= " + str(
                start_index[i - 1]) + " // End index = " + str(end_index[i - 1]))
            print("list size = " + str(len(original_df)))


def separate_tows(origin_path, saving_path, full_data=False):
    """
    We may have several tows in one single file, so for the sake of processing
    and tagging, it is necessary to separate these tows into several CSV files.
    This function separates the different tows by cutting all data under the
    mean (in translation: the data below the mean is intended to be the data
    when the fishing net is on the ship.) and saving each cut into a CSV
    file.
    :param path: path to the dataset
    :return: CSV files
    """
    if full_data:
        unseparated_df_list = dfm.get_all_dataframes(origin_path)
    else:
        unseparated_df_list = dfm.get_aperture_only(origin_path)
    df_index = 0

    for unseparated_df in unseparated_df_list:
        if not unseparated_df.empty:
            #TODO: Mirar corte optimo para o limite entre lances
            #Ademais, o nome pode ser tamen Abertura en vez de Estribor
            if full_data:
                towing_data_only = unseparated_df.where(
                    unseparated_df["Escalas(m)Estribor"] >
                    unseparated_df["Escalas(m)Estribor"].mean()/2)
            else:
                towing_data_only = unseparated_df.where(
                    unseparated_df["Escalas(m)"] >
                    unseparated_df["Escalas(m)"].mean()/2)

            start_index, end_index = limits_index(towing_data_only)
            if len(unseparated_df_list) > 10:
                save_to_csv(saving_path, df_index, unseparated_df, start_index, end_index)
            df_index += 1