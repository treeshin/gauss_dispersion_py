import numpy as np
from math import exp, pi

from data import winspeed, frequency
from calc_d import calc_d
from calc_he import calc_he
from calc_sigma import calc_sigma
from u_cor import u_cor 

hs = 68; w0 = 10; diameter = 2

sl = hs; pl = 10

x = np.arange(1,80000,1)

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
            doq[k] = doq[k] + frequency[5 * j + i, 0]/(100 * (2 * pi/16) * x[k])
    xoq[k] = 2.032 * xoq[k] / x[k]