import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm

df = pd.read_csv('ARTM_16dir.csv',
                    sep = ",",
                    header = None,
                    engine = 'python')

df = np.array(df)
index = df[0,:] # get index for distance
index=index.astype(int)
#orography = np.zeros((16,len(index))) # to ignore terrain heights
orography = df[1:17,:] # get terrain height data

orography_new = np.zeros((16,len(index)))
# wind directions are opposite to dispersion directions
for i in range(16):
    if i <= 7:
        orography_new[i+8,:] = orography[i,:]
    elif i > 7:
        orography_new[i-8,:] = orography[i,:]

orography = orography_new
