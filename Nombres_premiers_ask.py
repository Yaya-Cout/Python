#!/bin/python3
while True:
    nombre = input("Ton nombre à tester : ")
    try:
        nombre = int(nombre)
    except ValueError:
        print("Veuillez saisir un nombre valide")
        continue
    try:
        diviseurs = []
        for diviseur in range(1, nombre+1):
            division = nombre / diviseur
            # diviseurs.append(diviseur)
            if division == int(division):
                diviseurs.append(diviseur)
        if len(diviseurs) == 2:
            print("Le nombre est un nombre premier")
        else:
            print("Le nombre n'est pas un nombre premier")
        del diviseurs
        nombre += 1
    except KeyboardInterrupt:
        pass
        # print(nombre)
