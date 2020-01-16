import pickle
import pandas as pd
pickle_object_path = "/home/alex/Documents/Clase/TFG/Results/pickled_results"

with open(pickle_object_path, "rb") as file:
    scores_list = pickle.load(file)


df_total = pd.DataFrame(columns=["algorithm",
                               "error",
                               "gap",
                               "nEstimators",
                               "model",
                               "kernel",
                               "degree",
                               "coefficient",
                               "epsilon"])

for df in scores_list:
    min_gap = df["gap"].min()
    max_gap = df["gap"].max()
    for i in range(min_gap, max_gap, 5):
        df_gap = df.where(df["gap"] == i)
        best_gap_error = df_gap.where(df_gap["error"] == df_gap["error"].min()).dropna().iloc[0]
        df_total = df_total.append(best_gap_error)


df_final = pd.DataFrame(columns=["algorithm",
                               "error",
                               "gap",
                               "nEstimators",
                               "model",
                               "kernel",
                               "degree",
                               "coefficient",
                               "epsilon"])

for i in range(min_gap, max_gap, 5):
    df_gap_total = df_total.where(df_total["gap"] == i).dropna(how="all")
    best_gap_error_total = df_gap_total.where(df_gap_total["error"] == df_gap_total["error"].min()).iloc[0]
    df_final = df_final.append(best_gap_error_total)