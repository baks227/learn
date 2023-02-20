def slicer(cort):
    if len(cort) == 2:
        sym = cort[1]
        cort = cort[0]
    else:
        return []
    if cort.count(sym) == 1:
        return cort[cort.index(sym):]
    return cort[cort.index(sym):cort.index(sym,cort.index(sym)+1)+1]




#print(slicer(((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10),2)))