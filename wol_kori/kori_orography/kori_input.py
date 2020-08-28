import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('kori_2018.csv',
                    sep = ",",
                    header = 0,
                    engine = 'python')

df.columns = ['year','month','day','hour','minute',
                'temp_1point5','temp_10','direction_10','speed_10',
                'temp_58','direction_58','speed_58',
                'stability_temp']

df = np.array(df)

index = []
for i in range(len(df)):
    if df[i,10] == '-' or df[i,11] == '-':
        index = np.append(index,i)

if len(index) != 0:
    index  = index.astype(int)
    df = np.delete(df, index, axis = 0)

year = df[:,0]
month = df[:,1]
day = df[:,2]
hour = df[:,3]
minute = df[:,4]
temp_1point5 = df[:,5]
temp_10 = df[:,6]
direction_10 = df[:,7]
speed_10 = df[:,8]
temp_58 = df[:,9]
direction_58 = df[:,10]
speed_58 = df[:,11]
stability_temp = df[:,12]

#########################################
## Choose input here
stability = stability_temp
direction = direction_58.astype(float)
winspeed  = speed_58.astype(float)
kori_input = np.zeros([42, 16])
#########################################

for i in range(len(direction)):
    if direction[i] < 11.25 or direction[i] >= 348.75:
        l = 0
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 11.25 <= direction[i] < 33.75:
        l = 1
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 33.75 <= direction[i] < 56.25:
        l = 2
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 56.25 <= direction[i] < 78.75:
        l = 3
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 78.75 <= direction[i] < 101.25:
        l = 4
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 101.25 <= direction[i] < 123.75:
        l = 5
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 123.75 <= direction[i] < 146.25:
        l = 6
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 146.25 <= direction[i] < 168.75:
        l = 7
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 168.75 <= direction[i] < 191.25:
        l = 8
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 191.25 <= direction[i] < 213.75:
        l = 9
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 213.75 <= direction[i] < 236.25:
        l = 10
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 236.25 <= direction[i] < 258.75:
        l = 11
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 258.75 <= direction[i] < 281.25:
        l = 12
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1       
    elif 281.25 <= direction[i] < 303.75:
        l = 13
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 303.75 <= direction[i] < 326.25:
        l = 14
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
    elif 326.25 <= direction[i] < 348.75:
        l = 15
        if stability[i] == 'A':
            k = 0
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'B':
            k = 1
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'C':
            k = 2
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'D':
            k = 3
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'E':
            k = 4
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'F':
            k = 5
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
        elif stability[i] == 'G':
            k = 6
            if winspeed[i] < 1.0:
                j = 0
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 1.0 <= winspeed[i] < 2.0:
                j = 1
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 2.0 <= winspeed[i] < 4.0:
                j = 2
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 4.0 <= winspeed[i] < 8.0:
                j = 3
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 8.0 <= winspeed[i] < 16.0:
                j = 4
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1
            elif 16.0 <= winspeed[i] < 32.0:
                j = 5
                kori_input[6*k+j,l] = kori_input[6*k+j,l] + 1

winspeed = np.array([
    0.5, 1.5, 3.0, 6.0, 12.0, 24.0
])
kori_input = kori_input.astype(int)
sumsum = sum(sum(kori_input))