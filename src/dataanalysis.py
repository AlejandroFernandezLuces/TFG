from dataframemanager import DataframeManager
import matplotlib.pyplot as plt
import math

path = "/home/alex/Documents/Clase/TFG/Dataset/iskra/"

aa = DataframeManager.get_all_dataframes(path)


a = aa[1]

itemdrop =a.where(a["Escalas(m)Estribor"] > a["Escalas(m)Estribor"].mean())

i = 0
nonnan_index = []
while i < len(itemdrop):
    if not math.isnan(itemdrop["Escalas(m)Estribor"][i]):
        nonnan_index.append(i)
    i += 1

end_index = []
start_index = []
start_index.append(nonnan_index[0])
for i in range(1, len(nonnan_index) - 1):
    if nonnan_index[i] + 1 != nonnan_index[i + 1]:
        end_index.append(nonnan_index[i])
    if nonnan_index[i] - 1 != nonnan_index[i - 1]:
        start_index.append(nonnan_index[i])
end_index.append(nonnan_index(len(nonnan_index) - 1))
for i in range(len(end_index)):
    df = a[start_index[i]:end_index[i]]

"""
fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(itemdrop["Escalas(m)Estribor"])
axs[1].plot(a["Escalas(m)Estribor"])"""