import pandas as pd
import numpy as np
import math

def separate_with_mod(data, mod=2):
    """Funcion ad hoc para separar as duas variables cas que tratamos na
    primeira iteracion e ver as posibilidades do arima"""
    exog = []
    endog = []
    for elem in data:
        sub_exog = np.array([])
        sub_endog = np.array([])
        for elem2 in elem:
            sub_endog = np.append(sub_endog, elem2[0])
            sub_exog = np.append(sub_exog, elem2[1])
        #endog = np.append(endog,sub_endog)
        #exog = np.append(exog,sub_exog)
        endog.append(sub_endog)
        exog.append(sub_exog)
    #endog = endog[~np.isnan(endog)]
    #exog = exog[~np.isnan(exog)]
    ex_size = len(exog)
    en_size = len(endog)
    limit = min(ex_size, en_size)
    endog = endog[0:limit]
    exog = exog[0:limit]
    return exog, endog

def train_data(train):
    exog, endog = separate_with_mod(train)
    return endog, exog

def test_data(test):
    exog, endog = separate_with_mod(test)
    return endog, exog