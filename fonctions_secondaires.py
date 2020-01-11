import operator

def best_definition(liste_tuple):
    """ Sélectionne les mots ayant la plus forte valeur d'aprés une liste de \
tupples (mot/valeur)"""

    liste_tuple.sort(key=operator.itemgetter(1),reverse=True)
    definitions_retenues=[]
    valeur_retenue=liste_tuple[0][1]

    for (argument, valeur) in liste_tuple:
        if valeur==valeur_retenue:
            definitions_retenues.append(argument)
    return definitions_retenues

if __name__=="__main__":
    liste=[('meuble', 3), ('objet', 3), ('rectangle', 2), ('miel', -2)]
    A=best_definition(liste)
    print(A)

