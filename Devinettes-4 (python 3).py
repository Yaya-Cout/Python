﻿def main():
    import random
    import webbrowser

    # webbrowser.open("file:///home/neo/Documents/Python/Commandes.html")
    webbrowser.open("Commandes.html")
    Erreur = 10
    rejouer = "rejouer"
    point = 0
    credit = 0
    commands = 0
    nbtour = 0
    Erreur2 = 1
    print("Bienvenue dans ce jeu de devinette")

    print('Pour voir les commands rapides taper "commands"')
    while rejouer == "rejouer":

        try:

            def afficheCommandes():
                global commands

                if commands == 1:
                    print("")
                    print("Vous avez déja visionné les commands")
                    print(
                        "taper « credit » pour visionner les crédits;\
                        taper « nouvelle partie » pour commancer une novelle\
                             partie; taper « quitter » pour quitter; taper\
                                  commands pour voir les commands et\
                                       « aide » pour voir l "
                        + "' "
                        + "aide\
                                            complète."
                    )
                    #                print('taper "credit" pour visionner les crédits;\
                    # taper"nouvelle partie" pour commancer une novelle partie;\
                    #  taper"quitter" pour quitter;taper commands pour voir les commands\
                    #  taper commands pour voir les commands et « aide » pour voir l'+"'"\
                    # +'aide complète')
                    print("")
                else:
                    print("")
                    print(
                        "taper « credit » pour visionner les crédits;\
                        taper « nouvelle partie » pour commancer une novelle\
                             partie; taper « quitter » pour quitter; taper \
                                 commands pour voir les commands\
                                      et « aide » pour voir l "
                        + "' "
                        + "aide \
                                          complète."
                    )
                    commands = 1
                    print("")

            def aide():
                webbrowser.open("Commandes.html")

            def tour(rejouer, secret, commands, credit, point, Erreur, Erreur2):
                """Tour de jeu"""
                while rejouer == "rejouer":
                    nombre = input("Quel est ton nombre: ")

                    if nombre == "aide":
                        aide()
                        continue

                    if nombre == "credit" and credit == 1:
                        print("")
                        print("Vous avez déja visionné les credits")
                        print(
                            "Cree par Yaya.Cout à l'aide du livre:'Programer\
                                 avec python en s'amusant'"
                        )
                        print("")

                    elif nombre == "credit":
                        print("")
                        print(
                            "Cree par Yaya.Cout à l'aide du livre:'Programer\
                                 avec python en s'amusant'"
                        )
                        print("")
                        credit = 1

                    elif nombre == "commands":
                        afficheCommandes()
                        continue

                    # elif nombre == "commands" and commands==1:
                    #     print("")
                    #     print("Vous avez déja visionné les commands")
                    #     print('taper "credit" pour visionner les crédits;\
                    # taper"novelle partie" pour commancer une novelle \
                    # partie; taper"quitter" pour quitter;taper commands\
                    #  pour voir les commandes')
                    #     print("")
                    #
                    # elif nombre == "commands":
                    #     print("")
                    #     print('taper "credit" pour visionner les crédits;\
                    # taper"novelle partie" pour commancer une novelle\
                    #  partie; taper"quitter" pour quitter;taper commands\
                    #  pour voir les commandes')
                    #     commands=1
                    #     print("")

                    elif nombre == "nouvelle partie":
                        print("Le nombre etait " + str(secret))
                        print(
                            "Vous avez "
                            + str(point)
                            + " point"
                            + ("" if point < 2 else "s")
                        )
                        dificulte = input("Quel est ton niveau de dificulté: ")
                        secret = random.randint(1, int(dificulte))
                        continue

                    elif nombre == "quitter":
                        print("Le nombre etait: " + str(secret))
                        print(
                            "Vous avez "
                            + str(point)
                            + " point"
                            + ("" if point < 2 else "s")
                        )
                        rejouer = ""
                        return (Erreur, Erreur2, rejouer)

                    try:
                        nb = int(nombre)
                    except ValueError:
                        print("\n\t Et la, c'est le bug!\n")
                        continue

                    # elif str(secret) == nombre:
                    if secret == nb:
                        print("Bravo")
                        point = point + 5
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
                        return (Erreur, Erreur2, rejouer)

                    elif Erreur == 1 and point <= 1:
                        print("Vous avez perdu! Le nombre etait: " + str(secret))
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
                        #                nombre = input("Quel est ton nombre: ")
                        return (Erreur, Erreur2, rejouer)

                    elif Erreur == 1:
                        point = point - 2
                        print("Vous avez perdu! Le nombre etait: " + str(secret))
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
                        #                nombre = input("Quel est ton nombre: ")
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

                    # else:
                    #     print("Et la, c'est le bug!")

            """
                            if rejouer == "rejouer" or "azerty" or "Yaya.Cout":

                                Erreur=11
                                dificulte = input("Quel est ton niveau de\
                                     dificulté: ")
                                secret = random.randint(1,int(dificulte))
                                if Erreur>8:
                                    Erreur=16
                                elif Erreur>=5:
                                    Erreur=13
                            else:
                                break

                                or "azerty" or "Yaya.Cout"
            """

            while rejouer == "rejouer":
                dificulte = input("Quel est ton niveau de dificulté: ")
                if dificulte == "commands":
                    afficheCommandes()
                    continue

                if dificulte == "aide":
                    aide()
                    continue

                try:
                    dificulte = int(dificulte)
                    secret = random.randint(1, int(dificulte))
                except ValueError:
                    print("\n\t Et la, c'est le bug!\n")
                    continue

                Erreur, Erreur2, rejouer = tour(
                    rejouer, secret, commands, credit, point, Erreur, Erreur2
                )
                # Erreur = 11
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
                "\n Voulez vous démarrer en mode sans échec (o pour oui /\
                     autre chose pour non) ?"
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
