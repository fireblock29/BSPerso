def RechercheMin(tab):
    m = tab[0]
    i = 0
    index = 0
    for v in tab:
        if v < m:
            m = v
            index = i
        i = i + 1
    return index

