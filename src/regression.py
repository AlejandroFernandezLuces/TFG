from sklearn.model_selection import train_test_split
from src.models import randomforest, supportvectorregression as svr, \
    linearregression, neuralnetwork
from src.utils import windowroll, dfopener, scaler
import numpy as np


def main():
    df_path = "Dataset/csv_files_apertura/"
    dfs = dfopener.df_opener(df_path, min_sensor_reads=50)

    scaled_dfs, df_scaler = scaler.fit_scale(dfs)
    train, test = train_test_split(scaled_dfs, test_size=0.4, random_state=42)


    error_list = []
    gap_dict = {}
    kernels = ["rbf", "linear", "poly"]

    #hiperparametrizacion
    print("--------ADESTRAMENTO DE ALGORITMOS---------\n")
    for gap in range(0, 50, 5):
        error_dict = {}
        print("\n\n\n---Distancia de predicion => " + str(gap))
        X_train, y_train = windowroll.map_window(train, gap=gap)
        X_test, y_test = windowroll.map_window(test, gap=gap)

        """print("\n\nErros para RandomForest ->\n")
        for n_estimators in  range(100, 250, 50):
            error_rfr = randomforest.fit_predict_rfr(
                X_train,y_train, X_test, y_test, n_estimators)
            error_dict[error_rfr] = ["RFR", n_estimators]
    
        print("\n\nErros para linear regression ->\n")
        error_lr = linearregression.fit_predict_lr(
            X_train, y_train, X_test, y_test)
        error_dict[error_lr] = ["OLS"]"""

        print("\n\nErros para rede neuronal ->\n")
        error_nn = neuralnetwork.nn_fit( X_train, y_train, X_test, y_test)
        error_dict[error_nn] = ["NN"]
        """print("\n\nErros para SVR ---->\n")
        for kernel in kernels:
            for degree in range(2, 6):
                for coefficient in range(1,5):
                    for epsilon in np.arange(0.1, 1.5, 0.2):
                        error_svr =  svr.fit_predict_lr(
                            X_train,y_train, X_test, y_test,
                            kernel, degree, coefficient, epsilon)
                        error_dict[error_svr] = \
                            ["SVR", kernel, degree, coefficient, epsilon]"""
        gap_dict[gap] = error_dict
