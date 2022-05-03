def nb_repetitions(elt, tab):
    c = 0
    for e in tab:
        if e == elt:
            c = c + 1
    return c
