import featureextraction
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
import skimage
import seaborn as sns
import pandas as pd
import os
from PIL import Image
import PIL.ImageOps as ops
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def _df_opener(path):
    directory = os.listdir(path)
    df_list = []
    for file in directory:
        df = pd.read_csv(path + file)
        df_list.append(df)
    return df_list


def image_opener(path):
    directory = os.listdir(path)
    image_list = []
    path_list = []
    for file in directory:
        full_path = path + file
        path_list.append(full_path)
        image = skimage.data.load(full_path, as_gray=True)
        image = skimage.img_as_int(image)
        image = image.flatten()
        image_list.append(np.array(image))
    return image_list, path_list

def getImage(path):
    image =Image.open(path)
    image = image.resize((128, 128))
    #image = ops.invert(image)
    return OffsetImage(image)


images_path = "/home/alex/Documents/Clase/TFG/Dataset/graph_images/"
df_path = "/home/alex/Documents/Clase/TFG/Dataset/csv_files_apertura/"


#Training for the image dataset
image_list, path_list = image_opener(images_path)
train, test = train_test_split(image_list, train_size=0.60, test_size=0.40)
tsne = TSNE(verbose = 2)
X_embedded = tsne.fit_transform(train)

x = X_embedded[:,0]
y = X_embedded[:,1]

fig, ax = plt.subplots()
ax.scatter(x, y)

for x0, y0, path in zip(x, y,path_list):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    ax.add_artist(ab)
fig.savefig('myimage.svg', format='svg', dpi=1200)

#Training for the raw data
#df_list = _df_opener(df_path)
features = featureextraction.features(df_path)
train, test = train_test_split(features, train_size=0.60, test_size=0.40)
tsne = TSNE(verbose = 2)
X_embedded = tsne.fit_transform(train)

x = X_embedded[:,0]
y = X_embedded[:,1]

fig, ax = plt.subplots()
ax.scatter(x, y)

