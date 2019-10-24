import os
from txttocsv import TxtToCsv

path = "/home/alex/Documents/Clase/TFG/Dataset/iskra"

filenames = os.listdir(path)

for filename in filenames:
    TxtToCsv(path, filename).get_csv()