import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np

def print_gap_comparison(y_test, gap_dict, gap_dist, save=False):
    print("Gardando graficas... ")
    lines = ["-", "--", "-.", ":", "-r", "--r", "-.r", ":r", "-y", "--y", "-.y", ":y"]
    linecycler = cycle(lines)
    fig, ax = plt.subplots()
    ax.set_ylabel("Distancia(m)")
    ax.set_xlabel("Tempo(30s)")
    ax.plot(y_test[1:100], label="real")
    ax.set_title("Exemplo de lance real VS predito")
    ax.set_ylim(0)
    count = 0
    zeroes = []
    for i in gap_dist:
        if i != 0:
            pred = gap_dict[i][1:100]
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


def print_userlike(X_test, gap_dict, y_dict, error_dict,  gap_dist, elem_id, save=False, model_name="LR"):
    fig, ax = plt.subplots()
    ax.set_ylabel("Distancia(m)")
    ax.set_xlabel("Tempo(30s)")
    ax.plot(X_test, label="Datos reais historicos")
    ax.axvline(len(X_test) - 1, color="k", linestyle="--")
    ax.set_title("Exemplo de simulacion co Linear Regresion")
    ax.set_ylim(0)
    points_pred_x = []
    points_pred_y = []

    points_real_x = []
    points_real_y = []

    points_error_y_high = []
    points_error_y_low = []

    for i in gap_dist:
        points_pred_x.append(len(X_test) - 1 + i)
        points_pred_y.append(gap_dict[i][elem_id])

        points_real_x.append(len(X_test) - 1 + i)
        points_real_y.append(y_dict[i][elem_id])

        points_error_y_high.append(gap_dict[i][elem_id] + error_dict[i])
        points_error_y_low.append(gap_dict[i][elem_id] - error_dict[i])


    plt.plot(points_pred_x, points_pred_y, "r--", label="Predicion do algoritmo " + model_name)
    plt.plot(points_real_x, points_real_y, "g-", label="Datos reais futuro")
    plt.fill_between(points_pred_x,  points_error_y_high, points_error_y_low, color="c", label="Marxe de erro predito")

    #Liñas de erro no canto de area coloreada
    #plt.plot(points_pred_x, points_error_y_high, "c")
    #plt.plot(points_pred_x, points_error_y_low, "c")

    legend = ax.legend(loc='best', shadow=True, fontsize='medium')
