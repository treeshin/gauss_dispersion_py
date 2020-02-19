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