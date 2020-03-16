from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV


"""regression model for svr"""
def fit_predict_svr(X_train, y_train, X_test, y_test):
    kernels = ["rbf", "linear", "poly"]

    param_grid = {'kernel': kernels,
                 'C': [0.1, 1, 100, 1000],
                 'epsilon': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1,
                             0.5, 1, 5, 10],
                 'gamma': [0.0001, 0.001, 0.005, 0.1, 1, 3, 5]}
    gs = GridSearchCV(SVR(), param_grid=param_grid, verbose=2, n_jobs=-1)
    gs.fit(X_train, y_train)
    pred = gs.best_estimator_.predict(X_test)  # make prediction on test set
    error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
    return error, gs.best_params_