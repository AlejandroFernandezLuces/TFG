from dataframemanager import DataframeManager
import matplotlib.pyplot as plt


path = "/home/alex/Documents/Clase/TFG/Dataset/iskra/"

aa = DataframeManager.get_all_dataframes(path)


a = aa[0]

itemdrop =a.where(a["Escalas(m)Estribor"] > a["Escalas(m)Estribor"].mode())
plt.plot(itemdrop["Escalas(m)Estribor"])
plt.show()