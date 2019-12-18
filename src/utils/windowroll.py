import numpy as np

def _window(df, window_size=20, gap=0):
    window_list = []
    y_list = []
    df_size = df.shape[0]
    if df_size > window_size + gap:
        if not True in np.isnan(df):
            for i in range(df.shape[0] - window_size - gap - 1):
                window = np.ravel(df[i:i + window_size])
                y = df[gap + i + window_size + 1][0]
                window_list.append(window)
                y_list.append(y)
            return window_list, y_list
        else:
            return [], []
    else:
        return [], []


def _map_window(dfs, window_size=20, gap=0):
    X_list = []
    y_list = []
    for elem in dfs:
        X, y = _window(elem, window_size=window_size,gap=gap)
        for itemX in X:
            X_list.append(itemX)
        for itemY in y:
            y_list.append(itemY)
    return X_list, y_list