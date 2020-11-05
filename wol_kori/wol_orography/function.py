# ****************************************************************
"""
<function.py>
contains functions used in straight-line Gaussian dispersion.

- calc_sigma    returns sigma_z value at certain distance
                for each stability class.    

- calc_he       returns effective plume height at certain distance
                for each stability class, stack height, plume exit velocity,
                wind speed, and stack inner diameter.

- calc_d        returns relative deposition rate at certain distance
                for each stability class, and effective plume height.

- u_cor         returns corrected wind speed for each wind speed,
                desired height, measured height, and stability class.

- rfs           returns a set of random numbers with fixed sum.  

"""
# ****************************************************************

"""
CALC_SIGMA

"""
def calc_sigma(distance, stability):
    
    from math import log10

    if stability == 0:
        if distance < 100:
            a=0.192; b=0.936; c=0
        elif distance >= 100 and distance < 1000:
            a=0.00066; b=1.941; c=9.27
        elif distance >= 1000:
            a=0.00024; b=2.094; c=-9.6

    elif stability == 1:
        if distance < 100:
            a=0.156; b=0.922; c=0
        elif distance >= 100 and distance < 1000:
            a=0.0382; b=1.149; c=3.3
        elif distance >= 1000:
            a=0.055; b=1.098; c=2

    elif stability == 2:
        if distance < 100:
            a=0.116; b=0.905; c=0
        elif distance >= 100 and distance < 1000:
            a=0.113; b=0.911; c=0
        elif distance >= 1000:
            a=0.113; b=0.911; c=0

    elif stability == 3:
        if distance < 100:
            a=0.079; b=0.881; c=0
        elif distance >= 100 and distance < 1000:
            a=0.222; b=0.725; c=-1.7  
        elif distance >= 1000:
            a=1.26; b=0.516; c=-13

    elif stability == 4:
        if distance < 100:
            a=0.063; b=0.871; c=0            
        elif distance >= 100 and distance < 1000:
            a=0.211; b=0.678; c=-1.3
        elif distance >= 1000:
            a=6.73; b=0.305; c=-34

    elif stability == 5:
        if distance < 100:
            a=0.053; b=0.814; c=0
        elif distance >= 100 and distance < 1000:
            a=0.086; b=0.74; c=-0.35 
        elif distance >= 1000:
            a=18.05; b=0.18; c=-48.6        

    else:
        if distance < 100:
            a1=0.063; b1=0.871; c1=0
            a2=0.053; b2=0.814; c2=0
        elif distance >= 100 and distance < 1000:
            a1=0.211; b1=0.678; c1=-1.3
            a2=0.086; b2=0.74; c2=-0.35          
        elif distance >= 1000:
            a1=6.73; b1=0.305; c1=-34
            a2=18.05; b2=0.18; c2=-48.6
    
    if stability < 6:
        sigma = a * distance ** b + c
        if sigma > 1000:
            sigma = 1000
    else:
        sigma = 2 * log10(a2 * distance ** b2 + c2) - log10(a1 * distance ** b1 + c1)
        sigma = 10 ** sigma
        if sigma > 1000:
            sigma = 1000
    
    return(sigma)


"""
CALC_HE

"""
def calc_he(stability, hs, w0, winspeed, diameter, distance, direction, index, orography):
    
    import numpy as np

    if stability == 0 or stability == 1 or stability == 2 or stability == 3:
        if w0 >= 1.5 * winspeed:
            hprA = 1.44 * (w0/winspeed) ** (0.667) * (distance/diameter) ** (0.333) * diameter
            hprB = 3 * (w0/winspeed) * diameter
            hpr = min(hprA, hprB)
        else:
            C = 3 * (1.5 - w0/winspeed) * diameter
            hprA = 1.44 * (w0/winspeed) ** (0.667) * (distance/diameter) ** (0.333) * diameter - C
            hprB = 3 * (w0/winspeed) * diameter
            hpr = min(hprA, hprB)

    elif stability == 4:
        Fm = (w0 * diameter/2) ** 2
        S = 8.75 * 10 ** -4
        if w0 >= 1.5 * winspeed:
            hprA = 1.44 * (w0/winspeed) ** (0.667) * (distance/diameter) ** (0.333) * diameter
            hprB = 3 * (w0/winspeed) * diameter
            hprC = 4 * (Fm/S) ** (1/4)
            hprD = 1.5 * (Fm/winspeed) ** (0.333) * S ** (-0.1667)
            hpr = min([hprA, hprB, hprC, hprD])
        else:
            C = 3 * (1.5 - w0/winspeed) * diameter
            hprA = 1.44 * (w0/winspeed) ** (0.667) * (distance/diameter) ** (0.333) * diameter - C
            hprB = 3 * (w0/winspeed) * diameter
            hprC = 4 * (Fm/S) ** (1/4)
            hprD = 1.5 * (Fm/winspeed) ** (0.333) * S ** (-0.1667)
            hpr = min([hprA, hprB, hprC, hprD])

    elif stability == 5:
        Fm = (w0 * diameter/2) ** 2
        S = 1.75 * 10 ** -3
        if w0 >= 1.5 * winspeed:
            hprA = 1.44 * (w0/winspeed) ** (0.667) * (distance/diameter) ** (0.333) * diameter
            hprB = 3 * (w0/winspeed) * diameter
            hprC = 4 * (Fm/S) ** (1/4)
            hprD = 1.5 * (Fm/winspeed) ** (0.333) * S ** (-0.1667)
            hpr = min([hprA, hprB, hprC, hprD])
        else:
            C = 3 * (1.5 - w0/winspeed) * diameter
            hprA = 1.44 * (w0/winspeed) ** (0.667) * (distance/diameter) ** (0.333) * diameter - C
            hprB = 3 * (w0/winspeed) * diameter
            hprC = 4 * (Fm/S) ** (1/4)
            hprD = 1.5 * (Fm/winspeed) ** (0.333) * S ** (-0.1667)
            hpr = min([hprA, hprB, hprC, hprD])
    
    else:
            Fm = (w0*diameter/2) ** 2
            S = 2.45 * 10 ** - 3
            if w0 >= 1.5 * winspeed:
                hprA = 1.44 * (w0/winspeed) ** (0.667) * (distance/diameter) ** (0.333) * diameter
                hprB = 3 * (w0/winspeed) * diameter
                hprC = 4 * (Fm/S) ** (1/4)
                hprD = 1.5 * (Fm/winspeed) ** (0.333) * S ** (-0.1667)
                hpr = min([hprA, hprB, hprC, hprD])
            else:
                C = 3 * (1.5 - w0/winspeed) * diameter
                hprA = 1.44 * (w0/winspeed) ** (0.667) * (distance/diameter) ** (0.333) * diameter - C
                hprB = 3 * (w0/winspeed) * diameter
                hprC = 4 * (Fm/S) ** (1/4)
                hprD = 1.5 * (Fm/winspeed) ** (0.333) * S ** (-0.1667)
                hpr = min([hprA, hprB, hprC, hprD])
                
    a=np.where(index >= distance)[0]

    if len(a)==0:
        i = len(index)-1
        ht = orography[direction,i]
    else:
        i= min(a)
        ht = ((orography[direction,i]-orography[direction,i-1])/(index[i]-index[i-1]))*(distance-index[i-1])+orography[direction,i-1]

    if ht < 0:
        ht = 0

    he = hs + hpr - ht

    return(he)


"""
CALC_D

"""
def calc_d(distance, stability, he):
    
    from math import exp, log

    if he <= 15:
        if distance <= 999:
            D = exp(-9.07794+0.4357604*log(distance)-0.07881594*log(distance)*log(distance))
        elif distance > 999 and distance <= 9999:
            D = exp(-6.64143-0.2466506*log(distance)-0.03098147*log(distance)*log(distance))
        else:
            D = exp(-14.06597+1.10343*log(distance)-0.09031373*log(distance)*log(distance))

    elif he > 15 and he <= 45:
        if stability == 0 or stability == 1 or stability == 2:
            if distance <= 399:
                D = exp(-35.30917 + 9.57035*log(distance) - 0.8727484*log(distance)*log(distance))
            elif distance > 399 and distance <= 1999:
                D = exp(-3.946649 - 0.882866*log(distance))
            elif distance > 1999 and distance <= 4999:
                D = exp(-3.256392 - 1.20884*log(distance) + 0.03092014*log(distance)*log(distance))
            elif distance > 4999 and distance <= 12999:
                D = exp(-5.975507 - 0.6270642*log(distance))
            elif distance > 12999 and distance <= 19999:
                D = exp(12.1268 - 4.455138*log(distance) + 0.202586*log(distance)*log(distance))
            elif distance > 19999 and distance <= 59999:
                D = exp(-10.79479 + 0.01276474*log(distance) - 0.01497699*log(distance)*log(distance))
            else:
                D = exp(-54.18442 + 7.877314*log(distance) - 0.3715153*log(distance)*log(distance))
        elif stability == 3:
            if distance <= 199:
                D = exp(-42.9116 + 8.624134*log(distance) - 0.5286823*log(distance)*log(distance))
            elif distance > 199 and distance <= 399:
                D = exp(-45.080005 + 9.502915*log(distance) - 0.6178266*log(distance)*log(distance))
            elif distance > 399 and distance <= 1499:
                D = exp(-46.40474 + 10.93155*log(distance) - 0.818256*log(distance)*log(distance))
            elif distance > 1499 and distance <= 6999:
                D = exp(-12.06068 + 1.105205*log(distance) - 0.1167178*log(distance)*log(distance))
            elif distance > 6999 and distance <= 14999:
                D = exp(-4.148934 - 0.821923*log(distance))
            else:
                D = exp(-4.640997 - 0.7696691*log(distance))
        else: 
            if distance <= 4999:
                D = exp(-156.334 + 29.93037*log(distance) - 1.5483*log(distance)*log(distance))
            elif distance > 4999 and distance <= 8399:
                D = exp(-140.62 + 26.18382*log(distance) - 1.324944*log(distance)*log(distance))
            elif distance > 8399 and distance <= 41999:
                D = exp(-87.89882 + 15.38889*log(distance) - 0.7753119*log(distance)*log(distance))
            else:
                D = exp(-12.94973 + 1.26526*log(distance) - 0.1098207*log(distance)*log(distance))

    elif he > 45 and he <= 80:
        if stability == 0 or stability == 1 or stability == 2:
            if distance <= 399:
                D = exp(-30.4523 + 5.76941*log(distance) - 0.394098*log(distance)*log(distance))
            elif distance > 399 and distance <= 899:
                D = exp(-36.23268 + 8.23023*log(distance) - 0.6448782*log(distance)*log(distance))
            elif distance > 899 and distance <= 2999:
                D = exp(-1.56127 - 1.725164*log(distance) + 0.0694564*log(distance)*log(distance))
            elif distance > 2999  and distance <= 12999:
                D = exp(-5.807573 - 0.6388715*log(distance))
            elif distance > 12999 and distance <= 49999:
                D = exp(-0.2792892 - 1.959056*log(distance) + 0.07773757*log(distance)*log(distance))
            else:
                D = exp(-58.14337 + 8.633218*log(distance) - 0.4071184*log(distance)*log(distance))
        elif stability == 3:
            if distance <= 299:
                D = exp(-177.431 + 55.32239*log(distance) - 4.658777*log(distance)*log(distance))
            elif distance > 299 and distance  <= 999:
                D = exp(-58.73299 + 12.91683*log(distance) - 0.8705195*log(distance)*log(distance))
            elif distance > 999 and distance <= 2999:
                D = exp(-45.04643 + 9.088059*log(distance) - 0.6027659*log(distance)*log(distance))
            elif distance > 2999 and distance <= 19999:
                D = exp(-13.59167 + 1.164582*log(distance) - 0.1036683*log(distance)*log(distance))
            else:
                D = exp(-4.867893 - 0.7430947*log(distance))
        else:
            if distance <= 79999:
                D = exp(-357.2949 + 59.55312*log(distance) - 2.583151*log(distance)*log(distance))
            else:
                D = exp(-134.0653 + 20.00078*log(distance) - 0.8306277*log(distance)*log(distance))

    else:
        if stability == 0 or stability == 1 or stability == 2:
            if distance <= 399:
                D = exp(-57.04822 + 13.82261*log(distance) - 1.019382*log(distance)*log(distance))
            elif distance > 399 and distance <= 2999:
                D = exp(-35.26215 + 7.297182*log(distance) - 0.5343292*log(distance)*log(distance))
            elif distance > 2999 and distance <= 29999:
                D = exp(-1.488902 - 1.694416*log(distance) + 0.06353313*log(distance)*log(distance))
            else:
                D = exp(-45.70724 + 6.464447*log(distance) - 0.3122405*log(distance)*log(distance))
        elif stability == 3:
            if distance <= 1499:
                D = exp(-63.81157 + 11.90979*log(distance) - 0.6561428*log(distance)*log(distance))
            elif distance > 1499 and distance <= 9999:
                D = exp(-44.54416 + 8.03507*log(distance) - 0.4868832*log(distance)*log(distance))
            else:
                D = exp(-9.971805 + 0.1761891*log(distance) -0.04063289*log(distance)*log(distance))
        else:
            D = 0
    
    return(D)


"""
U_COR
"""

def u_cor(winspeed, sl, pl, stability):
    
    if stability == 0 or stability == 1 or stability == 2 or stability == 3:
        ex = 0.25
    else:
        ex = 0.50
    
    cor = (sl/pl) ** ex
    winspeed_corrected = cor * winspeed

    return(winspeed_corrected)


"""
CALC_ET

"""
def calc_Et(winspeed, w0, hs, hb):

    R = w0 / winspeed
    Et = 0
    if  R > 5  or hs >= 2 * hb:
        Et = 0 # elevated release only
    elif R <= 1:
        Et = 1 # ground release only
    elif R > 1 and R <= 1.5:
        Et = 2.58 - 1.58 * R
    elif R > 1.5 and R <= 5:
        Et = 0.3 - 0.06 * R
    
    return(Et)


"""
OPENTR

"""
def opentr(distance):
    from math import exp, log
    x = log(distance)
    if distance < 10000:
        opentr = exp(16.125 - (3.18951*x) + (0.1569306 * x * x))
        if opentr > 4:
            opentr = 4
    else:
        if distance >= 16090:
            opentr = 1
        else:
            opentr = exp(1.1865 - (0.1225 * x))

    return(opentr)



"""
RFS

"""
from random import *

def rfs(n,s):
    r = min(s,1)
    x = uniform(max(0, r-(r-s/n)*2), r)
    return n < 2 and [s] or sample([x] + rfs(n-1,s-x), n)
