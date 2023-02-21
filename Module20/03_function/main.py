def slicer(cort):
    if len(cort) == 2:
        sym = cort[1]
        cort = cort[0]
    else:
        return []
    if cort.count(sym) == 1:
        return cort[cort.index(sym):]
    return cort[cort.index(sym):cort.index(sym,cort.index(sym)+1)+1]

