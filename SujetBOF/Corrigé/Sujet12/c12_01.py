def moyenne (tab):
    n = len(tab)
    if n == 0:
        return "erreur"
    s = 0
    for v in tab:
        s = s + v
    return s / n