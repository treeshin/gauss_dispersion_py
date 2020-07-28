# calculates X/Q and D/Q in 16 directions
import sys
import numpy as np
from math import exp, pi, sqrt, log10, sin, cos
from matplotlib import pyplot as plt
from matplotlib import cm
from data import hs, w0, diameter, sl, pl, hb, winspeed, frequency, sumsum
from function import calc_sigma, calc_d, calc_he, u_cor, calc_Et, opentr
from ARTM_orography import orography, index

np.set_printoptions(threshold=np.inf)

## set x range here ############################
x = np.arange(1,5000,1) # x: distance in meters
################################################
xoq_elevated = np.zeros((len(x),16))
xoq_ground = np.zeros((len(x),16))
doq = np.zeros((len(x),16))
frequency = frequency
sumsum = sumsum
lenw = len(winspeed)
orography = orography
index = index

for l in range(16):
    for k in range(len(x)):
        for j in range(7): # atmospheric stability class : A - G
            winspeed_corrected = u_cor(winspeed, sl, pl, j) # wind speed correction based on power law
            sigma = calc_sigma(x[k],j) # sigma: dispersion coefficient
            sigma_new = min(sqrt((sigma * sigma) + \
                0.5 * (hb * hb) / pi), sigma * sqrt(3)) # sigma_new: dispersion coefficient for ground release
            for i in range(len(winspeed)):
                he = calc_he(j, hs, w0, winspeed_corrected[i], diameter, x[k], l, index, orography) # he: effective plume height
                D = calc_d(x[k], j, he) # D: deposition coefficient
                Et = calc_Et(winspeed_corrected[i], w0, hs, hb) # Et: ground release proportion
                xoq_elevated[k,l] = xoq_elevated[k,l] + (1 - Et) * frequency[lenw * j + i, l]/(sumsum * winspeed_corrected[i] * sigma)\
                    * exp(he ** 2 / (-2 * sigma ** 2))    
                xoq_ground[k,l] = xoq_ground[k,l] + Et * frequency[lenw * j + i, l]/(sumsum * winspeed_corrected[i] * sigma_new)
                doq[k,l] = doq[k,l] + frequency[lenw * j + i, l] * 1 * D /(sumsum * (2 * pi/16) * x[k])
        xoq_elevated[k,l] = 2.032 * 1 * xoq_elevated[k,l] / x[k]
        xoq_ground[k,l] = 2.032 * 1 * xoq_ground[k,l] / x[k]
xoq = xoq_elevated + xoq_ground
maxoq = np.amax(xoq)
locatexoq = np.where(xoq == maxoq)
print('maxoq is ',maxoq)
print('distance is ',x[locatexoq[0]])
print('direction is ',locatexoq[1])
maxdoq = np.amax(doq)
locatedoq = np.where(doq == maxdoq)
print('maxdoq is ',maxdoq)
print('distance is ',x[locatedoq[0]])
print('direction is ',locatedoq[1])

# 2D surface plot
azimuths = np.radians(np.linspace(0, 360, 17))
zeniths = x

r, theta = np.meshgrid(zeniths, azimuths)
values = np.zeros((azimuths.size, zeniths.size))

## set plot parameters here ###################################
for k in range(len(zeniths)):
    for l in range(len(azimuths)-1):
        # Wind direction is opposite to dispersion direction
        if l <= 7:
            values[l+8,k] = doq[k,l] ## select xoq or doq
        elif l > 7:
            values[l-8,k] = doq[k,l] ## select xoq or doq
    values[16,k] = values[0,k]
###############################################################

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))

# set clockwise polar coordinate
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

## colorbar level setting ########################################
lev = [c for c in np.arange(0,maxdoq*1.1,maxdoq/10, dtype=float)]
##################################################################

cs = ax.contourf(theta, r, values, levels = lev, cmap = 'viridis')
cbaxes = fig.add_axes([0.88, 0.1, 0.03, 0.8]) 
cbar = fig.colorbar(cs, cax = cbaxes)

plt.show()
