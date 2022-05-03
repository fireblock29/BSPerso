def verifie(tab):
    n = len(tab)
    if n == 1:
        return True
    for i in range(n-1):
        if tab[i]>tab[i+1]:
            return False
    return True

