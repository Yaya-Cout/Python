def main():
    import random

    Erreur = 10
    rejouer = "rejouer"
    point = 0
    nbtour = 0
    Erreur2 = 1
    lettre = "A"
    lettre_nombre = 2
    lettre_nombre2 = 0
    print("Bienvenue dans ce jeu d'équation")
    while rejouer == "rejouer":
        try:

            def Quel_est_le_nombre():
                nombre = input("Quel est le nombre " + lettre + " ? ")
                return nombre

            def tour(rejouer, secret, point, Erreur, Erreur2):
                """Tour de jeu"""
                while rejouer == "rejouer":
                    nombre = Quel_est_le_nombre()
                    if nombre == "nouvelle partie":
                        print("Le nombre " + lettre + " etait " + str(secret))
                        print(
                            "Vous avez "
                            + str(point)
                            + " point"
                            + ("" if point < 2 else "s")
                        )
                        dificulte = input("Quel est ton niveau de dificulté: ")
                        return (Erreur, Erreur2, rejouer)

                    elif nombre == "quitter":
                        print("Le nombre " + lettre + " etait " + str(secret))
                        print(
                            "Vous avez "
                            + str(point)
                            + " point"
                            + ("" if point < 2 else "s")
                        )
                        rejouer = ""
                        return (Erreur, Erreur2, rejouer)

                        # elif str(secret) == nombre:
                    if secret == nb and lettre_nombre == lettre_nombre2:
                        print("Bravo")
                        point = point + 5
                        print(
                            "Vous avez "
                            + str(point)
                            + " point"
                            + ("" if point < 2 else "s")
                        )
                        rejouer = input(
                            "Veux tu rejouer ? Tape pour rejouer pour rejouer,\
                                tape autre chose pour arreter. "
                        )
                        return (Erreur, Erreur2, rejouer)

                    if secret == nb:
                        Erreur = 10
                        print("Bravo")
                        point = point + 1
                        print(
                            "Vous avez "
                            + str(point)
                            + " point"
                            + ("" if point < 2 else "s")
                        )
                        secret = random.randint(1, int(dificulte))
                        continue

                    elif Erreur == 1:
                        point = point - 2
                        print(
                            "Vous avez perdu! Le nombre "
                            + lettre
                            + " etait: "
                            + str(secret)
                        )
                        print(
                            "Vous avez "
                            + str(point)
                            + " point"
                            + ("" if point < 2 else "s")
                        )
                        rejouer = input(
                            "Veux tu rejouer ? Tape pour rejouer pour rejouer\
                            ,tape autre chose pour arreter. "
                        )
                        #            nombre = input("Quel est ton nombre: ")
                        return (Erreur, Erreur2, rejouer)

                    #        if secret == int(nombre):
                    #                print("Correct")
                    # elif str(secret) > nombre:
                    elif secret > nb:
                        print("Trop petit")
                        Erreur = Erreur - 1
                        print("Il vous reste " + str(Erreur) + " essais")
                        Erreur2 = Erreur2 + 1

                    elif str(secret) < nombre:
                        print("Trop grand")
                        Erreur = Erreur - 1
                        Erreur2 = Erreur2 + 1
                        print("Il vous reste " + str(Erreur) + " essais")

            while rejouer == "rejouer":
                dificulte = input("Quel est ton niveau de dificulté: ")
                try:
                    dificulte = int(dificulte)
                    secret = random.randint(1, int(dificulte))
                except ValueError:
                    print("\n\t Et la, c'est le bug!\n")
                    continue
                Erreur, Erreur2, rejouer = tour(rejouer, secret, point, Erreur, Erreur2)
                if Erreur > 8:
                    Erreur = 16
                elif Erreur >= 5:
                    Erreur = 13
                nbtour = nbtour + 1
                Moyenne = float(int(Erreur2)) / float(int(nbtour))
                print("Ta moyenne est de " + str(Moyenne) + " erreurs")
                if Erreur > 8:
                    Erreur = 16
                elif Erreur >= 5:
                    Erreur = 13
                secret = random.randint(1, int(dificulte))

        except ValueError:
            print("Erreur de programme")
            sans_echec = input(
                "\n Voulez vous démarrer en mode sans échec\
                 (o pour oui / autre chose pour non) ?"
            )
            if sans_echec == "o":
                import random

                dificulte = 100
                secret = random.randint(1, int(dificulte))
                while True:
                    nombre = input("Quel est ton nombre: ")
                    try:
                        nb = int(nombre)
                    except ValueError:
                        print("Et la, c'est le bug!")
                        continue

                    if secret == nb:
                        print("Bravo")
                        try:
                            dificulte = int(dificulte)
                            dificulte = input("Quel est ton niveau de dificulté: ")
                            secret = random.randint(1, int(dificulte))
                        except ValueError:
                            print("\n\t Et la, c'est le bug!\n")
                            continue

                    elif secret > nb:
                        print("Trop petit")

                    elif str(secret) < nombre:
                        print("Trop grand")

            if sans_echec == "O":
                import random

                dificulte = 100
                secret = random.randint(1, int(dificulte))
                while True:
                    nombre = input("Quel est ton nombre: ")
                    try:
                        nb = int(nombre)
                    except ValueError:
                        print("Et la, c'est le bug!")
                        continue

                    if secret == nb:
                        print("Bravo")
                        try:
                            dificulte = int(dificulte)
                            dificulte = input("Quel est ton niveau de dificulté: ")
                            secret = random.randint(1, int(dificulte))
                        except ValueError:
                            print("\n\t Et la, c'est le bug!\n")
                            continue

                    elif secret > nb:
                        print("Trop petit")

                    elif str(secret) < nombre:
                        print("Trop grand")

            else:
                break


if __name__ == "__main__":
    main()
