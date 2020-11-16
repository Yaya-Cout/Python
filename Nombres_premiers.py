#!/bin/python3s
nombre = 2
try:
    while True:
        diviseurs = []
        for diviseur in range(1, nombre+1):
            division = nombre / diviseur
            # diviseurs.append(diviseur)
            if division == int(division):
                diviseurs.append(diviseurs)
        if len(diviseurs) == 2:
            print(nombre)
        del diviseurs
        nombre += 1
except KeyboardInterrupt:
    pass
    # print(nombre)
