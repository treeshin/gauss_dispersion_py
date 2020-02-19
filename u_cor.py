def u_cor(winspeed, sl, pl, stability):
    
    if stability == 0 or stability == 1 or stability == 2 or stability == 3:
        ex = 0.25
    else:
        ex = 0.50
    
    cor = (sl/pl) ** ex
    winspeed_corrected = cor * winspeed

    return(winspeed_corrected)