from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from math import sqrt

def fit_predict_lr(X_train, y_train, X_test, y_test, kernel="rbf",
                   degree=3, coeficient=1, epsilon=0.1):
    model = SVR(kernel, degree, C=coeficient,epsilon=epsilon)
    model.fit(X=X_train, y=y_train)
    pred = model.predict(X_test)  # make prediction on test set
    error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
    print("SVR---> RMSE value is:", error)
    return error