import numpy as np

def _window(df, window_size=20, gap=0):
    """
    Given one df, this function separates the df in several pieces with one
    point in the future of the signal as Y
    :param df: the signal to window
    :param window_size: the size of the window
    :param gap: samples ahead of the window
    :return: the windows and its Y
    """
    window_list = []
    y_list = []
    df_size = df.shape[0]
    if df_size > window_size + gap:
        if not True in np.isnan(df): #makes sure there is no nans in the df
            for i in range(df.shape[0] - window_size - gap - 1):
                window = np.ravel(df[i:i + window_size]) #flattens the df in the given segment
                y = df[gap + i + window_size + 1][1]
                window_list.append(window)
                y_list.append(y)
            return window_list, y_list
        else:
            return [], []
    else:
        return [], []


def map_window(dfs, window_size=20, gap=0):
    """
    Applies the window function to all the dataframes in the list
    :param dfs: list of dataframes
    :param window_size: desired size of the window
    :param gap: number of samples ahead to predict
    :return: the list with the X and the Y of the dataset
    """
    X_list = []
    y_list = []
    for elem in dfs:
        X, y = _window(elem, window_size=window_size,gap=gap)
        for itemX in X:
            X_list.append(itemX)
        for itemY in y:
            y_list.append(itemY)
    return X_list, y_list