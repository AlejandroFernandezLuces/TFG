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
    endog_train = np.array(endog_train)
    exog_train = np.array(exog_train)
    endog_test = np.array(endog_test)
    model = auto_arima(endog_train
                       ,exogenous=exog_train, start_p=1, start_q=1, max_p=7,
                        max_q=7, d=1, max_d=7, trace=True,
                        error_action="ignore", suppress_warnings = True,
                        stepwise = True,
                        verbose=2,
                        seasonal=False)

    pred = model.predict(n_periods=40)  # make prediction on test set
    print(pred)
    #error = sqrt(mean_squared_error(endog_test, pred))  # calculate rmse
    print("Arima---> RMSE value is:")
    return pred