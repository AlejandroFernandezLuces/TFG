from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

def fit_predict_lr(X_train, y_train, X_test, y_test):
    model = LinearRegression(n_jobs=-1)
    gs = GridSearchCV(LinearRegression(), param_grid={"fit_intercept":[True, False]}, verbose=2, n_jobs=-1)

    gs.fit(X=X_train, y=y_train)
    pred = gs.predict(X_test)  # make prediction on test set
    error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
    print("LR---> RMSE value is:", error)
    return  error, gs

def predict_lr(model, X_test):
    pred = model.predict(X_test)
    return pred