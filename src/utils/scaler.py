from sklearn.preprocessing import MinMaxScaler


def fit_scale(dfs):
    scaler = MinMaxScaler()
    scaled_dfs = []
    for elem in dfs:
        scaler.partial_fit(elem)
    for elem in dfs:
        df = scaler.transform(elem)
        scaled_dfs.append(df)
    return scaler, scaled_dfs