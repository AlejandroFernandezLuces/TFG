from pmdarima.arima import auto_arima
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np




def check_model(X_train, y_train):
    model = auto_arima(y_train,
                        exogenous=X_train, start_p=1, start_q=1, max_p=7,
                        max_q=7, d=1, max_d=7, trace=True,
                        error_action="ignore", suppress_warnings = True,
                        stepwise = True,
                        verbose=2,
                        seasonal=False)
    print(model.summary())


def fit_predict_arima(endog_train, exog_train, endog_test, exog_test):
    """
    As variables esoxenas non poden ser usadas debido a que na predicion
    non imos dispoñer de ningunha delas a priori
    :param endog_train:
    :param exog_train:
    :param endog_test:
    :param exog_test:
    :return:
    """
    endog_train = np.array(endog_train)
    exog_train = np.array(exog_train)
    endog_test = np.array(endog_test)

    model = auto_arima(endog_train[0]
                       , start_p=1, start_q=1, max_p=7,
                        max_q=7, d=1, max_d=7, trace=True,
                        error_action="ignore", suppress_warnings = True,
                        stepwise = True,
                        verbose=2,
                        seasonal=False)

    pred = model.predict(n_periods=40)  # make prediction on test set
    print(pred)
    #error = sqrt(mean_squared_error(endog_test, pred))  # calculate rmse
    #print("Arima---> RMSE value is:", error)
    #return error, model.params()