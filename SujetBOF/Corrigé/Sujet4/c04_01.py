def recherche(tab):
    t = []
    for i in range(1,len(tab)):
        diff = tab[i]-tab[i-1]
        if diff == 1:
            t.append((tab[i-1], tab[i]))
    return t