from sklearn.model_selection import train_test_split
from dataset_management import dataframemanager, towfileseparator
from src.models import randomforest, supportvectorregression as svr, \
    linearregression, sarimax
from src.utils import windowroll, dfopener, scaler, arima_data_manager, graphs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
from itertools import cycle


#def main():

raw_data = "Dataset/iskra/"
df_path = "Dataset/test/"
#towfileseparator.separate_tows("Dataset/iskra/", "Dataset/test/")
dfs = dfopener.df_opener(df_path, min_sensor_reads=50)
dfs_unscaled = []
for elem in dfs:
    if not isinstance(elem, list):
        if elem.size > 10:
            dfs_unscaled.append(elem.to_numpy())
scaled_dfs, df_scaler = scaler.fit_scale(dfs_unscaled)
train, test = train_test_split(dfs_unscaled, test_size=0.9, random_state=42)
test = test[50:60]
plt.plot(test[0].transpose()[1], "ro")


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


print("\n\n-------------------------------------------")
print(">>>>>>>>>>>>> APROXIMACION 1 <<<<<<<<<<<<<")
print("-------------------------------------------\n\n")


pred_list = []
y_test_list = []
X_test_list = []


fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
exp_list = [fib(i) for i in range(2,10)]
#exp_list = [20, 30, 40, 0]
gap_dict = {}
y_dict = {}
gap_list = []

for gap in exp_list:
    print("\n\n\n---Distancia de predicion => " + str(gap))
    X_train, y_train = windowroll.map_window(train,window_size=200, gap=gap)
    X_test, y_test = windowroll.map_window(test,window_size=200, gap=gap)


    print("\n\nErros para linear regression ->\n")
    error_lr, model_lr = linearregression.fit_predict_lr(
        X_train, y_train, X_test, y_test)
    df_aux = pd.DataFrame({"algorithm": "lr",
                           "error": [error_lr],
                           "gap": [gap]})
    #df_lr = df_lr.append(df_aux)
    pred = model_lr.predict(X_test)
    pred_list.append(pred)
    #y_test_list.append(y_test)
    #gap_list.append(pred)
    gap_dict[gap] = pred
    #y_dict[gap] = y_test

graphs.print_gap_comparison(y_test, gap_dict, exp_list, save=False)

"""
print("\n\nErros para RandomForest ->\n")
error_rfr_list = []
error_rfr, rfr_params, rfr_model = randomforest.fit_predict_rfr(X_train,y_train, X_test, y_test)
df_aux = pd.DataFrame({"algorithm":"rfr",
                       "error":[error_rfr],
                       "gap":[gap],
                       "params": [rfr_params]})
df_rfr = df_rfr.append(df_aux)
pred = randomforest.predict_rfr(rfr_model, X_test)
pred_list.append(pred)
y_test_list.append(y_test)
gap_dict[gap] = pred"""



"""print("\n\nErros para SVR ---->\n")

error_svr, params_svr =  svr.fit_predict_svr(
X_train,y_train, X_test, y_test)
df_aux = pd.DataFrame({"algorithm": "svr",.....
                       "error": [error_svr],
                       "gap": [gap],
                       "params":[params_svr]})

df_svr = df_svr.append(df_aux)
print("<<<<<<<< End of battery training >>>>>>>>>>>>>")
result_list = [df_lr, df_rfr, df_svr]

file = open("Results/pickled_results_aprox1", "wb")
pickle.dump(result_list, file)
file.close()"""



"""print("\n\n-------------------------------------------")
print(">>>>>>>>>>>>> APROXIMACION 2 <<<<<<<<<<<<<")
print("-------------------------------------------\n\n")

for gap in range(0, 50, 5):
    print("\n\n\n---Distancia de predicion => " + str(gap))
    endog_train, exog_train = arima_data_manager.train_data(train)
    endog_test, exog_test = arima_data_manager.test_data(test)
    sarimax.fit_predict_arima(endog_train, exog_train, endog_test, exog_test)"""




"""print("\n\n-------------------------------------------")
print(">>>>>>>>>>>>> APROXIMACION 3 <<<<<<<<<<<<<")
print("-------------------------------------------\n\n")
for gap in range(0, 50, 5):
    print("\n\n\n---Distancia de predicion => " + str(gap))
    X_train, y_train =    
"""

