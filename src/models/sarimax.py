from pmdarima.arima import auto_arima
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np


def separate_with_mod(train, mod=2):
    """Funcion ad hoc para separar as duas variables cas que tratamos na
    primeira iteracion e ver as posibilidades do arima"""
    exog = []
    endog = []
    for i in range(0, len(train) - 1):
        sub_endog = []
        sub_exog = []
        for j in range(0, len(train[i])):
            if j % mod == 0:
                sub_exog.append(train[i][j])
            else:
                sub_endog.append(train[i][j])
        exog.append(sub_exog)
        endog.append(sub_endog)
    return np.array(exog), np.array(endog)


def check_model(X_train, y_train):
    model = auto_arima(y_train,
                        exogenous=X_train, start_p=1, start_q=1, max_p=7,
                        max_q=7, d=1, max_d=7, trace=True,
                        error_action="ignore", suppress_warnings = True,
                        stepwise = True,
                        verbose=2,
                        seasonal=False)
    print(model.summary())


def fit_predict_arima(X_train, y_train, X_test, y_test, model_coefficients=[0, 1, 1]):
    X_train_lon, X_train_abr = separate_with_mod(X_train)
    X_test_lon, X_test_abr = separate_with_mod(X_test)


    X_train_arima = np.concatenate((X_test_abr, X_train_lon), axis=0)

    #if model_coefficients == []:
    model = auto_arima(y_train
                       ,exogenous=X_train_arima, start_p=1, start_q=1, max_p=7,
                        max_q=7, d=1, max_d=7, trace=True,
                        error_action="ignore", suppress_warnings = True,
                        stepwise = True,
                        verbose=2,
                        seasonal=False)
    print(model.summary())
    """else:
        model = ARIMA(X_train_en,  (model_coefficients[0],
                                model_coefficients[1],
                                model_coefficients[2]),
                      exog=X_train_ex)"""
    pred = model.predict(n_periods=X_test_ex.shape[0], exogenous=X_test_ex)  # make prediction on test set
    error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
    print("Arima---> RMSE value is:", error)
    return error