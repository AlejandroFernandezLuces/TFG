from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from math import sqrt

def fit_predict_rfr(X_train, y_train, X_test, y_test, estimators=100):
    model = RandomForestRegressor(n_estimators=estimators,
                                  warm_start=True,
                                  verbose=0,
                                  n_jobs=-1)
    model.fit(X=X_train, y=y_train)
    pred = model.predict(X_test)  # make prediction on test set
    error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
    print("RFR---> RMSE value for " + str(estimators) + " estimators is:", error)
    return error