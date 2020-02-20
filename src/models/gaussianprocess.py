from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ExpSineSquared, RationalQuadratic
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np


def fit_predict_gp(X_train, y_train, X_test, y_test):
    grid = {"alpha": [1e0, 1e-1, 1e-2, 1e-3],
              "kernel": [[ExpSineSquared(l, p)
                         for l in np.logspace(-2, 2, 10)
                         for p in np.logspace(0, 2, 10)],
                        [RationalQuadratic(l, a)
                         for l in np.logspace(0, 2, 10)
                         for a in np.logspace(0, 2, 10)]]}


    gs = GridSearchCV(GaussianProcessRegressor(), grid, verbose=5, n_jobs=-1)
    gs.fit(X_train, y_train)
    pred = gs.best_estimator_.predict(X_test)  # make prediction on test set
    error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
    return error, gs.best_params_