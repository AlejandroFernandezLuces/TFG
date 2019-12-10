import matplotlib.pyplot as plt
import pandas as pd
import os


"""Test para ver como vai o tema do t-SNE, omellor danos un bo clustering"""


origin_path = "/home/alex/Documents/Clase/TFG/Dataset/csv_files_apertura/"
images_path = "/home/alex/Documents/Clase/TFG/Dataset/graph_images/"

filenames = os.listdir(origin_path)

for file in filenames:
    dataframe = pd.read_csv(origin_path + file)
    if not dataframe.empty:
        fig, axs = plt.subplots(2)
        axs[0].set_title("Apertura(brazas)")
        axs[0].plot(dataframe["Escalas(m)"])
        axs[1].set_title("Loxitude de cable(metros)")
        try:
            axs[1].plot(dataframe["Datos1(Fa)"])
        except:
            try:
                axs[1].plot(dataframe["Datos1(°)"])
            except:
                axs[1].plot(dataframe["Datos1(m)"])

        plt.savefig(images_path + file[:-4] + ".png")
        plt.close(fig)
