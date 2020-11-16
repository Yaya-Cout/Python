#!/bin/python3
nombre = 3
nombres_premiers = [1, 2]
print(2)
try:
    while True:
        diviseurs = []
        for diviseur in nombres_premiers:
            division = nombre / diviseur
            if division == int(division):
                diviseurs.append(diviseur)
        if len(diviseurs) == 1:
            print(nombre)
            nombres_premiers.append(nombre)
        del diviseurs
        nombre += 2
except KeyboardInterrupt:
    pass
    # print(nombre)
