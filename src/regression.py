from sklearn.model_selection import train_test_split
from models import randomforest, supportvectorregression as svr, \
    linearregression
from utils import windowroll, dfopener, scaler



df_path = "/home/alex/Documents/Clase/TFG/Dataset/csv_files_apertura/"
dfs = dfopener._df_opener(df_path, min_sensor_reads=50)

scaled_dfs = scaler.fit_scale(dfs)
train, test = train_test_split(scaled_dfs, test_size=0.4, random_state=42)


rfr_rmse = []
lr_rmse = []
svr_rmse = []

#hiperparametrizacion
print("--------ADESTRAMENTO DE ALGORITMOS---------\n")
for gap in range(0, 50, 5):
    print("\n\n\n---Distancia de predicion => " + str(gap))
    X_train, y_train = windowroll.map_window(train, gap=gap)
    X_test, y_test = windowroll.map_window(test, gap=gap)

    print("\n\nErros para RandomForest ->\n")
    for i in  range(100, 250, 50):
        rfr_rmse.append(
            randomforest.fit_predict_rfr(
                X_train,y_train, X_test, y_test, i))

    print("\n\nErros para linear regression ->\n")
    lr_rmse.append(
        linearregression.fit_predict_lr(X_train, y_train, X_test, y_test))

    print("\n\nErros para SVR ---->\n")
    svr_rmse.append(
        svr.fit_predict_lr(X_train,y_train, X_test, y_test, )
    )