import featureextraction
import dataset_management.filemanager as filemanager
import dataset_management.dataframemanager as dataframemanager
import dataset_management.towfileseparator as towfileseparator
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

path = "/home/alex/Documents/Clase/TFG/Dataset/iskra/"
saving_path = "/home/alex/Documents/Clase/TFG/Dataset/csv_files/"
saving_path2 = "/home/alex/Documents/Clase/TFG/Dataset/csv_files_apertura/"
#filemanager.get_all_csv(path)
#towfileseparator.separate_tows(path,saving_path2, full_data=False)
points = featureextraction.features(saving_path2)


pca = PCA(n_components=2)
principal_components = pca.fit_transform(points)
principal_df = pd.DataFrame(data=principal_components, columns=["component_1", "component_2"])

x = principal_df.values
min_max_scaler = MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
principal_df = pd.DataFrame(data=x_scaled,columns=["component_1", "component_2"])

select_algorithm = 0
if select_algorithm:
    # create kmeans object
    kmeans = KMeans(n_clusters=2).fit(principal_df)# fit kmeans object to data
    labels = kmeans.predict(principal_df)


    points["is_bad"] = labels

    colores = ["red", "blue", "yellow", "cyan", "black"]

    asignar = []
    for row in labels:
        asignar.append(colores[row])
    plt.scatter(principal_df["component_1"], principal_df["component_2"], c=asignar)

    #Solo para ficheiros etiquetados
    """asignar2 = []
    for row in points["is_bad"].values.tolist():
        row = int(row)
        asignar2.append(colores[row])
    plt.scatter(principal_df["component_1"], principal_df["component_2"], c=asignar2)"""

else:
    # Hierarchical clustering for the same dataset
    # creating a dataset for hierarchical clustering
    dataset2_standardized = points# needed imports

    # you probably won't need this
    np.set_printoptions(precision=5, suppress=True)  # suppress scientific float notation#creating the linkage matrix
    H_cluster = linkage(dataset2_standardized,'ward')
    plt.title('Hierarchical Clustering Dendrogram (truncated)')
    plt.xlabel('sample index or (cluster size)')
    plt.ylabel('distance')
    dendrogram(
        H_cluster,
        truncate_mode='lastp',  # show only the last p merged clusters
        p=5,  # show only the last p merged clusters
        leaf_rotation=90.,
        leaf_font_size=12.,
        show_contracted=True,  # to get a distribution impression in truncated branches
    )
plt.show()
