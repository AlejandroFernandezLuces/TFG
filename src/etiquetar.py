import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy import signal
import towfileseparator
import dataframemanager

path = "/home/alex/Documents/Clase/TFG/Dataset/iskra/"
saving_path =  "/home/alex/Documents/Clase/TFG/Dataset/csv_files/"
saving_path2 = "/home/alex/Documents/Clase/TFG/Dataset/csv_files_tagged/"

towfileseparator.separate_tows(path, saving_path)

filenames = os.listdir(saving_path)
filenames.sort()
for csv in filenames:
    dataframe = pd.read_csv(saving_path + csv)
    if len(dataframe) > 1:
        fig, axs = plt.subplots(2)
        axs[0].set_title("Apertura(brazas)")
        axs[0].plot(dataframe["Datos1(Fa)Estribor"])
        axs[1].set_title("Loxitude de cable(metros)")
        axs[1].plot(dataframe["Escalas(m)Estribor"])
        plt.pause(0.05)
        bad_input = True
        while(bad_input):
            embarra = input("Embarra? ->")
            if embarra == "1" or embarra == "0":
                bad_input = False
                csv = csv + "-embarra=" + embarra + ".csv"
                dataframe.to_csv(saving_path2 + csv)
            elif embarra == "2":
                bad_input = False
            else:
                print("Wrong input")
        print("hola")
        plt.show()
        plt.close()
