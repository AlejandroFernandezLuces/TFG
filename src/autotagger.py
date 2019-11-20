import os
import pandas as pd
import sklearn.preprocessing as preprocessing
import scipy.signal as signal
import pywt
import matplotlib.pyplot as plt
import numpy as np

saving_path = "/home/alex/Documents/Clase/TFG/Dataset/csv_files_tagged/"

filenames = os.listdir(saving_path)

Y = []
x = []
for filename in filenames:
    dataframe = pd.read_csv(saving_path + filename)
    longitud = dataframe["Escalas(m)Estribor"]
    try:
        apertura = dataframe["Datos1(Fa)Estribor"]
        longitud = dataframe["Escalas(m)Estribor"]
    except:
        try:
            apertura = dataframe["Datos1(m)Estribor"]
        except:
            apertura = dataframe["Datos1(°)Estribor"]
    apertura = apertura.dropna()
    print(apertura)

    #Normalizar apertura de portas
    min_max_scaler_apertura = preprocessing.MinMaxScaler()


    apertura = apertura.values
    apertura = apertura.reshape(-1, 1)
    apertura_scaled = min_max_scaler_apertura.fit_transform(apertura)

    apertura_mean = apertura_scaled.mean()
    apertura_std = apertura_scaled.std()
    apertura_var = apertura_scaled.var()


    #Fourier  non aporta nada, porque non hai frecuencias coas que traballar
    """apertura_fourier = np.fft.fft(apertura_scaled)

    apertura_fourier_real_mean = apertura_fourier.real.mean()
    apertura_fourier_imag_mean = apertura_fourier.std.mean()

    apertura_fourier_real_std = apertura_fourier.imag.mean()
    apertura_fourier_imag_std = apertura_fourier.imag.std()"""

    apertura_hist_scaled = np.histogram(apertura_scaled, bins = 15)

    widths = np.arange(1, 31)
    apertura_cwt, apertura_cwt_freq = pywt.cwt(apertura_scaled, widths, "mexh")
    apertura_cwt = apertura_cwt[0]

    apertura_cwt_mean = apertura_cwt.mean()
    apertura_cwt_std = apertura_cwt.std()
    apertura_cwt_var = apertura_cwt.var()

    apertura_hist_cwt = np.histogram(apertura_cwt, bins = 15)

    min_max_scaler_longitud = preprocessing.MinMaxScaler()

    longitud = longitud.values
    longitud = longitud.reshape(-1, 1)
    longitud_scaled = min_max_scaler_longitud.fit_transform(longitud)

    longitud_mean = longitud_scaled.mean()
    longitud_std = longitud_scaled.std()
    longitud_var = longitud_scaled.var()

    longitud_hist_scaled = np.histogram(longitud_scaled, bins=15)

    widths = np.arange(1, 31)
    longitud_cwt, longitud_cwt_freq = pywt.cwt(longitud_scaled, widths, "mexh")
    longitud_cwt = longitud_cwt[0]

    longitud_cwt_mean = longitud_cwt.mean()
    longitud_cwt_std = longitud_cwt.std()
    longitud_cwt_var = longitud_cwt.var()

    longitud_hist_cwt = np.histogram(longitud_cwt, bins=15)
    #Asociar dato a sua etiqueta
    if filename[-5] == "0":
        lance_problematico = 0
    else:
        lance_problematico = 1
