import numpy as np
from math import exp, pi
from matplotlib import pyplot as plt
from data import winspeed, frequency
from function import calc_sigma, calc_d, calc_he, u_cor, rfs

for iteration in range(100):

    r = rfs(35, 100)
    print(sum(r))
    for j in range(7):
        for i in range(5):
            frequency[5 * j + i, 0] = r[5 * j + i]

    hs = 68; w0 = 10; diameter = 2
    sl = hs; pl = 68

    x = np.arange(1,2000,10)

    xoq = np.zeros(len(x))
    doq = np.zeros(len(x))

    for k in range(len(x)):
        for j in range(7):
            winspeed_corrected = u_cor(winspeed, sl, pl, j)
            sigma = calc_sigma(x[k],j)
            for i in range(5):
                he = calc_he(j, hs, w0, winspeed_corrected[0,i], diameter, x[k])
                D = calc_d(x[k], j, he)
                xoq[k] = xoq[k] + frequency[5 * j + i, 0]/(100 * winspeed_corrected[0,i] * sigma) * exp(he ** 2 / (-2 * sigma ** 2))    
                doq[k] = doq[k] + frequency[5 * j + i, 0] * D /(100 * (2 * pi/16) * x[k])
        xoq[k] = 2.032 * xoq[k] / x[k]

# plot the results
    plt.plot(x,xoq)

plt.show()
