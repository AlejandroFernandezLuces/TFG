import pandas as pd
import os
from sklearn.model_selection import train_test_split
#import required packages
from sklearn import neighbors
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

df_path = "/home/alex/Documents/Clase/TFG/Dataset/csv_files_apertura/"

def _df_opener(path):
    directory = os.listdir(path)
    df_list = []
    for file in directory:
        df = pd.read_csv(path + file)
        if df.shape[0] > 20:
            df_list.append(df)
    return df_list


def _window(df, window_size = 20, prediction_range = 1):
    window_list = []
    y_list = []
    df_size = df.shape[0]
    if df_size > window_size + prediction_range:
        df = df.drop(["Tiempo"], axis=1)
        for i in range(df.shape[0] - prediction_range):
            window = df[i:i + window_size]
            y = df.iloc[window_size + prediction_range]
            window_list.append(window)
            y_list.append(y)
    return window_list, y_list


window_list = []
y_list = []
for elem in _df_opener(df_path):
    window, y = _window(elem)
    window_list.append(window)
    y_list.append(y)


X_train, X_test, y_train, y_test = train_test_split(
    window_list, y_list, test_size=0.33, random_state=42)

rmse_val = [] #to store rmse values for different k
for K in range(19,20):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors = K)
    print("First iteration")
    model.fit(X_train, y_train)  #fit the model
    pred=model.predict(X_test) #make prediction on test set
    error = sqrt(mean_squared_error(y_test,pred)) #calculate rmse
    rmse_val.append(error) #store rmse values
    print('RMSE value for k= ' , K , 'is:', error)