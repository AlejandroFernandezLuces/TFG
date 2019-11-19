import os
import pandas as pd
import sklearn.preprocessing as preprocessing
import numpy
import scipy.signal as signal
saving_path = "/home/alex/Documents/Clase/TFG/Dataset/csv_files_tagged/"

filenames = os.listdir(saving_path)

Y = []
x = []
for filename in filenames:
    dataframe = pd.read_csv(saving_path + filename)
    try:
        apertura = dataframe["Datos1(Fa)Estribor"]
    except:
        try:
            apertura = dataframe["Datos1(m)Estribor"]
        except:
            apertura = dataframe["Datos1(°)Estribor"]
    apertura = apertura.dropna()
    print(apertura)

    #Normalizar apertura de portas
    min_max_scaler = preprocessing.MinMaxScaler()


    apertura = apertura.values
    apertura_scaled = min_max_scaler.fit_transform(apertura)

    apertura_mean = apertura_scaled.mean()
    apertura_std = apertura_scaled.std()

    apertura_scaled = apertura_scaled.reshape(1, -1)
    apertura_fourier = numpy.fft.fft(apertura_scaled)

    apertura_fourier_real_mean = apertura_fourier.real.mean()
    apertura_fourier_imag_mean = apertura_fourier.std.mean()

    apertura_fourier_real_std = apertura_fourier.imag.mean()
    apertura_fourier_imag_std = apertura_fourier.imag.std()

    #apertura_cwt = signal.cwt(apertura_scaled)

    #Asociar dato a sua etiqueta
    if filename[-5] == "1":
        Y.append(dataframe)
    elif filename[-5] == "0":
        x.append(dataframe)