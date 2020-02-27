import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np

def print_gap_comparison(y_test, gap_dict, gap_dist, save=False):
    print("Gardando graficas... ")
    lines = ["-", "--", "-.", ":", "-r", "--r", "-.r", ":r", "-y", "--y", "-.y", ":y"]
    linecycler = cycle(lines)
    fig, ax = plt.subplots()
    ax.set_ylabel("metros")
    ax.set_xlabel("medicions")
    ax.plot(y_test, label="real")
    ax.set_title("Exemplo de lance real VS predito")
    ax.set_xlim(0, len(y_test))
    count = 0
    zeroes = []
    for i in gap_dist:
        if i != 0:
            pred = gap_dict[i]
            zeroes = [np.nan]*i
            zeroes = np.array(zeroes)
            zeroes = np.append(zeroes, pred)
            ax.plot(zeroes, next(linecycler), label="gap: "+str(i))
            count += i
    legend = ax.legend(loc='best', shadow=True, fontsize='medium')
    if save:
        plt.savefig("Graficos/LR prediction-real/fig_gap_2.svg")
        plt.close()
    else:
        plt.show()

def print_gap_binary(y_dict, gap_dict, gap_dist, save=False):
    print("Gardando graficas... ")
    lines = ["-", "--", "-.", ":", "-r", "--r", "-.r", ":r", "-y", "--y", "-.y", ":y"]
    linecycler = cycle(lines)

    count = 0
    for i in gap_dist:
        fig, ax = plt.subplots()
        ax.set_ylabel("metros")
        ax.set_xlabel("medicions")
        y_test = y_dict[i]
        pred = gap_dict[i]
        ax.plot(y_test, label="real")
        ax.plot(pred, next(linecycler), label="gap: "+str(i))
        count += 1
        legend = ax.legend(loc='best', shadow=True, fontsize='medium')
        plt.savefig("Graficos/LR prediction-real/fig_gaps"+str(i) +".svg", format="svg")
        plt.close()