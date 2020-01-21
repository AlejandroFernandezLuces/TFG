from sklearn.model_selection import train_test_split, GridSearchCV
from src.models import randomforest, supportvectorregression as svr, \
    linearregression, neuralnetwork
from src.utils import windowroll, dfopener, scaler
import numpy as np
import pandas as pd
import pickle

#def main():
df_path = "Dataset/csv_files_apertura/"
dfs = dfopener.df_opener(df_path, min_sensor_reads=50)

scaled_dfs, df_scaler = scaler.fit_scale(dfs)
train, test = train_test_split(scaled_dfs, test_size=0.3, random_state=42)

error_list = []
gap_dict = {}
kernels = ["rbf", "linear", "poly"]

# hiperparametrizacion
print("--------ADESTRAMENTO DE ALGORITMOS---------\n")
df_rfr = pd.DataFrame(columns=["algorithm",
                               "error",
                               "gap",
                               "nEstimators"])

df_lr = pd.DataFrame(columns=["algorithm",
                              "error",
                              "gap"])

df_rna = pd.DataFrame(columns=["algorithm",
                               "error",
                               "gap",
                               "model"])

df_svr = pd.DataFrame(columns=["algorithm",
                               "error",
                               "gap",
                               "kernel",
                               "degree",
                               "coefficient",
                               "epsilon"])


"""---------- Primeira aproximacion -------------------

Emprega o xanelado para obter o punto de predicion. A entrada sera un anaco
do sinal de tamaño fixo. Esta xanela irase movendo ao longo do sinal ata 
completala. A saida e un punto posterior a esta xanela, o cal se predi 
empregando unicamente a sua correspondente xanela. Escollense diversos puntos
de prediccion. O ideal seria unha aproximacion logaritmica no canto de 
aritmetica.(1, 2, 4, 8....)"""

for gap in range(0, 50, 5):
    error_dict = {}
    print("\n\n\n---Distancia de predicion => " + str(gap))
    X_train, y_train = windowroll.map_window(train, gap=gap)
    X_test, y_test = windowroll.map_window(test, gap=gap)

    print("\n\nErros para linear regression ->\n")
    error_lr = linearregression.fit_predict_lr(
        X_train, y_train, X_test, y_test)
    df_aux = pd.DataFrame({"algorithm": "lr",
                           "error": [error_lr],
                           "gap": [gap]})
    df_lr = df_lr.append(df_aux)

    print("\n\nErros para RandomForest ->\n")
    error_rfr_list = []
    error_rfr, rfr_params = randomforest.fit_predict_rfr(X_train,y_train, X_test, y_test)
    df_aux = pd.DataFrame({"algorithm":"rfr",
                           "error":[error_rfr],
                           "gap":[gap],
                           "params": [rfr_params]})
    df_rfr = df_rfr.append(df_aux)
    
    print("\n\nErros para SVR ---->\n")

    error_svr, params_svr =  svr.fit_predict_svr(
    X_train,y_train, X_test, y_test)
    df_aux = pd.DataFrame({"algorithm": "svr",
                           "error": [error_svr],
                           "gap": [gap],
                           "params":[params_svr]})

    df_svr = df_svr.append(df_aux)
    print("<<<<<<<< End of battery training >>>>>>>>>>>>>")
    result_list = [df_lr, df_rfr, df_rna, df_svr]

    file = open("Results/pickled_results", "wb")
    pickle.dump(result_list, file)
    file.close()