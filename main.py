from sklearn.model_selection import train_test_split
from src.models import randomforest, supportvectorregression as svr, \
    linearregression, neuralnetwork, sarimax
from src.utils import windowroll, dfopener, scaler
import numpy as np
import pandas as pd
import pickle

#def main():
df_path = "Dataset/csv_files_apertura/"
dfs = dfopener.df_opener(df_path, min_sensor_reads=50)

scaled_dfs, df_scaler = scaler.fit_scale(dfs)
train, test = train_test_split(scaled_dfs, test_size=0.95, random_state=42)

error_list = []
gap_dict = {}
kernels = ["rbf", "linear", "poly"]

# hiperparametrizacion
print("--------ADESTRAMENTO DE ALGORITMOS---------\n")
df_rfr = pd.DataFrame(columns=["error",
                               "gap",
                               "nEstimators"])

df_lr = pd.DataFrame(columns=["error",
                              "gap"])

df_rna = pd.DataFrame(columns=["error",
                               "gap",
                               "model"])

df_svr = pd.DataFrame(columns=["error",
                               "gap",
                               "kernel",
                               "degree",
                               "coefficient",
                               "epsilon"])


for gap in range(0, 50, 5):
    error_dict = {}
    print("\n\n\n---Distancia de predicion => " + str(gap))
    X_train, y_train = windowroll.map_window(train, gap=gap)
    X_test, y_test = windowroll.map_window(test, gap=gap)

    print("\n\nErros para linear regression ->\n")
    error_lr = linearregression.fit_predict_lr(
        X_train, y_train, X_test, y_test)
    df_aux = pd.DataFrame({"error": [error_lr],
                           "gap": [gap]})
    df_lr = df_lr.append(df_aux)

    print("\n\nErros para RandomForest ->\n")
    error_rfr_list = []
    for n_estimators in  range(100, 250, 50):
        error_rfr = randomforest.fit_predict_rfr(
            X_train,y_train, X_test, y_test, n_estimators)
        df_aux = pd.DataFrame({"error":[error_rfr],
                               "gap":[gap],
                               "nEstimators": [n_estimators]})
        df_rfr = df_rfr.append(df_aux)

    print("\n\nErros para rede neuronal ->\n")
    error_nn_sim = neuralnetwork.fit_predict_nn(X_train, y_train, X_test, y_test)
    error_nn_com = neuralnetwork.fit_predict_nn(X_train, y_train, X_test, y_test, use_model="complex")
    df_aux = pd.DataFrame({"error": [error_nn_sim],
                           "gap": [gap],
                           "model": ["simple"]})
    df_rna = df_rna.append(df_aux)
    df_aux = pd.DataFrame({"error": [error_nn_com],
                           "gap": [gap],
                           "model": ["complex"]})
    df_rna = df_rna.append(df_aux)
    
    print("\n\nErros para SVR ---->\n")
    for kernel in kernels:
        for degree in range(2, 6):
            for coefficient in range(1,5):
                for epsilon in np.arange(0.1, 1.5, 0.2):
                    error_svr =  svr.fit_predict_svr(
                    X_train,y_train, X_test, y_test,
                    kernel, degree, coefficient, epsilon)
                    df_aux = pd.DataFrame({"error": [error_nn_sim], 
                                           "gap": [gap],
                                           "kernel":[kernel],
                                           "degree":[degree],
                                           "coefficient":[coefficient],
                                           "epsilon":[epsilon]})
                    df_svr = df_svr.append(df_aux)
    result_list = [df_lr, df_rfr, df_rna, df_svr]

    file = open("Results/pickled_results", "wb")
    pickle.dump(result_list, file)
    file.close()