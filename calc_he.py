def calc_he(stability, hs, w0, winspeed, diameter, distance):
    
    if stability == 0 or stability == 1 or stability == 2 or stability == 3:
        if w0 >= 1.5 * winspeed:
            hprA = 1.44 * (w0/winspeed) ** (2/3) * (distance/diameter) ** (1/3) * diameter
            hprB = 3 * (w0/winspeed) * diameter
            hpr = min(hprA, hprB)
        else:
            C = 3 * (1.5 - w0/winspeed) * diameter
            hprA = 1.44 * (w0/winspeed) ** (2/3) * (distance/diameter) ** (1/3) * diameter - C
            hprB = 3 * (w0/winspeed) * diameter
            hpr = min(hprA, hprB)

    elif stability == 4:
        Fm = (w0 * diameter/2) ** 2
        S = 8.7 * 10 ** -4
        if w0 >= 1.5 * winspeed:
            hprA = 1.44 * (w0/winspeed) ** (2/3) * (distance/diameter) ** (1/3) * diameter
            hprB = 3 * (w0/winspeed) * diameter
            hprC = 4 * (Fm/S) ** (1/4)
            hprD = 1.5 * (Fm/winspeed) ** (1/3) * S ** (-1/6)
            hpr = min([hprA, hprB, hprC, hprD])
        else:
            C = 3 * (1.5 - w0/winspeed) * diameter
            hprA = 1.44 * (w0/winspeed) ** (2/3) * (distance/diameter) ** (1/3) * diameter - C
            hprB = 3 * (w0/winspeed) * diameter
            hprC = 4 * (Fm/S) ** (1/4)
            hprD = 1.5 * (Fm/winspeed) ** (1/3) * S ** (-1/6)
            hpr = min([hprA, hprB, hprC, hprD])

    elif stability == 5:
        Fm = (w0 * diameter/2) ** 2
        S = 1.75 * 10 ** -3
        if w0 >= 1.5 * winspeed:
            hprA = 1.44 * (w0/winspeed) ** (2/3) * (distance/diameter) ** (1/3) * diameter
            hprB = 3 * (w0/winspeed) * diameter
            hprC = 4 * (Fm/S) ** (1/4)
            hprD = 1.5 * (Fm/winspeed) ** (1/3) * S ** (-1/6)
            hpr = min([hprA, hprB, hprC, hprD])
        else:
            C = 3 * (1.5 - w0/winspeed) * diameter
            hprA = 1.44 * (w0/winspeed) ** (2/3) * (distance/diameter) ** (1/3) * diameter - C
            hprB = 3 * (w0/winspeed) * diameter
            hprC = 4 * (Fm/S) ** (1/4)
            hprD = 1.5 * (Fm/winspeed) ** (1/3) * S ** (-1/6)
            hpr = min([hprA, hprB, hprC, hprD])
    
    else:
            Fm = (w0*diameter/2) ** 2
            S = 2.45 * 10 ** - 3
            if w0 >= 1.5 * winspeed:
                hprA = 1.44 * (w0/winspeed) ** (2/3) * (distance/diameter) ** (1/3) * diameter
                hprB = 3 * (w0/winspeed) * diameter
                hprC = 4 * (Fm/S) ** (1/4)
                hprD = 1.5 * (Fm/winspeed) ** (1/3) * S ** (-1/6)
                hpr = min([hprA, hprB, hprC, hprD])
            else:
                C = 3 * (1.5 - w0/winspeed) * diameter
                hprA = 1.44 * (w0/winspeed) ** (2/3) * (distance/diameter) ** (1/3) * diameter - C
                hprB = 3 * (w0/winspeed) * diameter
                hprC = 4 * (Fm/S) ** (1/4)
                hprD = 1.5 * (Fm/winspeed) ** (1/3) * S ** (-1/6)
                hpr = min([hprA, hprB, hprC, hprD])

    he = hs + hpr
    return(he)