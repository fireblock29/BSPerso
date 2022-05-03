def nombre_de_mots(phrase):
    c = 0
    n = len(phrase)
    for i in range(n):
        if phrase[i] == ' ':
            c = c + 1
    if phrase[n-1] != '?' and  phrase[n-1] != '!':
        c = c + 1
    return c
