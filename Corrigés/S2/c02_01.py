def moyenne(lst):
    somme = 0
    coef = 0
    for c in lst:
        somme = somme + c[0]*c[1]
        coef = coef + c[1]
    return somme/coef