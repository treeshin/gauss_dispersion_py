import numpy as np

hs = 68 # hs: stack height
w0 = 10 # w0: plume exit velocity
diameter = 2 # diameter: stack inner diameter

sl = hs # sl: release height
pl = 58 # pl: measured height of JFD

hb = 0 # hb: building height

# XOQDOQ default wind speed
winspeed = np.array([
    0.5, 1.5, 3.0, 6.0, 12.0, 24.0
])

# When using separate input file,
# frequency table will be generated there
frequency = np.array([
    # Stability A
    [29,11,9,9,13,16,36,67,52,47,40,30,27,36,36,54],
    [25,10,8,13,9,14,125,104,59,69,77,43,37,35,32,52],
    [9,5,6,7,8,31,248,89,93,166,201,165,163,95,42,47],
    [0,0,2,4,1,3,33,6,17,31,32,51,48,24,6,4],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # Stability B
    [4,0,0,2,2,2,8,0,6,2,10,1,4,4,2,4],
    [4,2,2,1,0,1,26,13,13,11,8,12,20,20,5,9],
    [21,3,2,4,4,11,52,24,32,38,48,55,61,53,21,16],
    [3,0,1,1,5,2,20,10,15,25,35,56,53,36,3,6],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # Stability C
    [4,1,1,3,2,4,6,8,7,6,8,6,4,5,5,6],
    [8,9,3,6,7,17,32,15,21,22,20,10,13,17,17,5],
    [16,26,10,15,20,23,74,21,36,68,79,79,89,70,35,16],
    [17,17,27,18,39,52,69,27,63,78,156,306,299,197,51,32],
    [0,0,0,0,2,0,2,0,4,1,27,67,68,42,25,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # Stability D
    [6,1,1,2,4,2,4,2,6,1,2,1,5,0,1,5],
    [7,0,1,1,1,1,12,2,5,5,2,6,12,6,8,3],
    [7,2,3,4,8,7,36,14,20,25,36,45,59,69,21,14],
    [6,4,1,6,23,37,52,15,22,33,47,93,111,107,33,17],
    [0,0,0,0,2,2,3,0,0,0,0,4,4,6,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # Stability E
    [26,2,2,2,1,3,6,2,3,0,0,1,1,1,1,2],
    [10,4,4,0,0,9,5,8,13,6,5,5,6,2,9,5],
    [24,3,2,5,14,26,18,15,26,16,24,34,38,44,31,19],
    [0,1,0,1,16,24,29,4,2,15,10,42,41,38,12,10],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # Stability F
    [2,6,3,3,4,3,6,3,2,3,1,1,1,1,0,2],
    [15,19,12,2,8,12,12,2,11,6,5,5,5,5,12,9],
    [20,6,0,2,21,33,17,13,17,18,22,24,24,30,16,25],
    [0,0,0,0,9,4,6,0,0,1,1,5,5,2,3,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    # Stability G
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
])

sumsum = sum(sum(frequency))