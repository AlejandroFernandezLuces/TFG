from keras import Sequential
from keras.layers import Dense, MaxPool1D, Conv1D, LSTM, Flatten, Dropout, Embedding
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np


def complex_model(input_shape):
    model = Sequential()
    #model.add(Dense(2, input_dim=40, activation="softmax"))

    model.add(Embedding(input_shape[0], 1, input_length=40))
    model.add(Conv1D(32, kernel_size=3, padding="same", activation="relu"))
    model.add(MaxPool1D(pool_size=3))
    model.add(Conv1D(32, kernel_size=3, padding="same", activation="relu"))
    model.add(MaxPool1D(pool_size=3))
    model.add(LSTM(50, return_sequences=True))
    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.45))
    model.add(Dense(1, activation="sigmoid"))

    model.compile(loss='binary_crossentropy', optimizer='adam',
                  metrics=['accuracy'])
    return model

def simple_model(input_shape):
    model = Sequential()
    model.add(Dense(2, input_dim=input_shape[0], activation="softmax"))
    model.add(Dense(8, activation="relu"))
    model.add(Dense(1, activation="relu"))
    model.compile(loss='binary_crossentropy', optimizer='adam',
                  metrics=['accuracy'])
    return model

def nn_fit(X_train, y_train, X_test, y_test, use_model="simple"):
    X_train = np.array(X_train)
    if use_model == "simple":
        model = simple_model(X_train.shape)
    elif use_model == "complex":
        model = complex_model(X_train.shape)
    model.fit(X_train, y_train, verbose=0, epochs=50, batch_size=128)
    X_test = np.array(X_test)
    pred = model.predict(X_test)  # make prediction on test set
    error = sqrt(mean_squared_error(y_test, pred))  # calculate rmse
    print("NN---> RMSE value is:", error)
    return error