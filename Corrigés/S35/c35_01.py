def moyenne(tab):
    s = 0
    for v in tab:
        s = s + v
    return s / len(tab)

assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5