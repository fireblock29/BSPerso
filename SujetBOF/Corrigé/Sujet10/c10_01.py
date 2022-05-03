def occurence_lettres (phrase):
    d = {}
    for c in phrase:
        if c in d:
            d[c] = d[c] + 1
        else :
            d[c] = 1
    return d
