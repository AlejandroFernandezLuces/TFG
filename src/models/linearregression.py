from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt

def fit_predict_lr(X_train, y_train, X_test, y_test):
    model = LinearRegression(n_jobs=-1)
    model.fit(X=X_train, y=y_train)
    pred = model.predict(X_test)  # make prediction on test set
    error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
    print("LR---> RMSE value is:", error)
    return error