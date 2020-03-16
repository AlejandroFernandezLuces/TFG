import os
import pandas as pd
import sklearn.preprocessing as preprocessing
import scipy.signal as signal
import pywt
import matplotlib.pyplot as plt
import numpy as np



def cwt_transf(signal):
    widths = np.arange(1, 31)
    signal_cwt, signal_cwt_freq = pywt.cwt(signal, widths, "mexh")
    signal_cwt = signal_cwt[0]
    return signal_cwt, signal_cwt_freq

def scale_signal(signal):
    signal = signal.values
    signal = signal.reshape(-1, 1)
    min_max_scaler = preprocessing.MinMaxScaler()
    scaled_signal = min_max_scaler.fit_transform(signal)
    return scaled_signal, min_max_scaler

def extract_stat_features(signal_scaled):
    signal_hist = np.histogram(signal_scaled, bins = 5)

    return signal_scaled.mean(), signal_scaled.std(), \
           signal_scaled.var(), signal_hist[0]


def features(path):
    feature_list_list = []
    filenames = os.listdir(path)
    for filename in filenames:
        feature_list = np.array([])
        dataframe = pd.read_csv(path + filename)
        if not dataframe.empty:
            if len(dataframe.columns) == 3:
                longitud = dataframe[dataframe.columns[1]]
                apertura = dataframe[dataframe.columns[2]]
            else:
                try:
                    apertura = dataframe["Datos1(Fa)Estribor"]
                    longitud = dataframe["Escalas(m)Estribor"]
                except:
                    try:
                        apertura = dataframe["Datos1(m)Estribor"]
                    except:
                        try:
                            apertura = dataframe["Datos1(°)Estribor"]
                        except:
                            apertura = dataframe["Escalas(m)"]
            apertura = apertura.dropna()
            if apertura.size > 0:
                #Features de apertura
                apertura_scaled, min_max_scaler_apertura = scale_signal(apertura)
                apertura_mean, apertura_std, apertura_var, apertura_hist = extract_stat_features(apertura_scaled)
                feature_list = np.append(feature_list, [apertura_mean, apertura_std, apertura_var])
                feature_list = np.append(feature_list, apertura_hist)
                #Fourier  non aporta nada, porque non hai frecuencias coas que traballar

                #features de apertura wavelet
                apertura_cwt, apertura_cwt_freq = cwt_transf(apertura_scaled)
                apertura_cwt_mean, apertura_cwt_std, apertura_cwt_var, apertura_cwt_hist = \
                    extract_stat_features(apertura_cwt)
                feature_list = np.append(feature_list, [apertura_cwt_mean, apertura_cwt_std, apertura_cwt_var])
                feature_list = np.append(feature_list, apertura_cwt_hist)



                #features de longitud
                longitud_scaled, min_max_scaler_longitud = scale_signal(longitud)
                longitud_mean, longitud_std, longitud_var, longitud_hist \
                    = extract_stat_features(longitud_scaled)

                feature_list = np.append(feature_list, [longitud_mean, longitud_std, longitud_var])
                feature_list = np.append(feature_list, longitud_hist)

                #features de longitud wavelet
                longitud_cwt, longitud_cwt_freq = cwt_transf(longitud_scaled)
                longitud_cwt_mean, longitud_cwt_std, longitud_cwt_var, longitud_cwt_hist \
                    = extract_stat_features(longitud_cwt)
                feature_list = np.append(feature_list, [longitud_cwt_mean, longitud_cwt_std, longitud_cwt_var])
                feature_list = np.append(feature_list, longitud_cwt_hist)

                #Asociar dato a sua etiqueta
                if filename[-5] == "0":
                    lance_problematico = 0
                else:
                    lance_problematico = 1
                feature_list = np.append(feature_list, lance_problematico)
                feature_list = np.array(feature_list)
                feature_list_list.append(feature_list)

            #painfully ad-hoc
            feature_names = ["apertura_mean", "apertura_std", "apertura_var",
                             "apertura_hist_1", "apertura_hist_2",
                             "apertura_hist_3", "apertura_hist_4",
                             "apertura_hist_5",
                             "apertura_cwt_mean", "apertura_cwt_std",
                             "apertura_cwt_var", "apertura_cwt_hist_1",
                             "apertura_cwt_hist_2", "apertura_cwt_hist_3",
                             "apertura_cwt_hist_4", "apertura_cwt_hist_5",
                             "longitud_mean", "longitud_std", "longitud_var",
                             "longitud_hist_1", "longitud_hist_2",
                             "longitud_hist_3", "longitud_hist_4",
                             "longitud_hist_5",
                             "longitud_cwt_mean", "longitud_cwt_std",
                             "longitud_cwt_var", "longitud_cwt_hist_1",
                             "longitud_cwt_hist_2", "longitud_cwt_hist_3",
                             "longitud_cwt_hist_4", "longitud_cwt_hist_5", "is_bad"]

        dataframe = pd.DataFrame(data=feature_list_list, columns=feature_names)
    return dataframe



