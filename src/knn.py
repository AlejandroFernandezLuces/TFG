import featureextraction
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
points = featureextraction.features()


# create kmeans object
kmeans = KMeans(n_clusters=2)# fit kmeans object to data
kmeans.fit(points)

