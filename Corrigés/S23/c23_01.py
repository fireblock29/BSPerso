def max_dico(dico):
    m = 0
    nom_m = ""
    for nom,v in dico.items():
        if v > m:
            m = v
            nom_m = nom
    return (nom_m,m)
