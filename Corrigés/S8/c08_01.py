def recherche(elt,tab):
    indice = 0
    for v in tab:
        if v == elt:
            return indice
        indice = indice + 1
    return -1
