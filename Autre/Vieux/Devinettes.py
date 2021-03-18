def main():
    import random

    Erreur = 10
    rejouer = "rejouer"
    point = 0
    credit = 0
    commands = 0

    print("Bienvenue dans ce jeu de devinette")
    dificulte = input("Quel est ton niveau de dificulté:")
    if dificulte == "credit":
        print("")
        print(
            "Cree par Yaya.Cout à l'aide du livre:'Programer avec python en\
             s'amusant'"
        )
        print("")
        credit = 1

    elif dificulte == "commands":
        print(
            'taper "credit" pour visionner les crédits;\
             taper "novelle partie" pour commancer une novelle partie; \
                 taper "quitter" pour quitter; taper commands pour voir les \
                     commandes'
        )
        commands = 1

    print('Pour voir les commands taper "commands"')
    secret = random.randint(1, int(dificulte))
    # while True:
    while rejouer == "rejouer":
        nombre = input("Quel est ton nombre: ")
        if nombre == "credit" and credit == 1:
            print("")
            print("Vous avez déja visionné les credits")
            print(
                "Cree par Yaya.Cout à l'aide du livre:'Programer avec python\
                     en s'amusant'"
            )
            print("")

        elif nombre == "credit":
            print("")
            print(
                "Cree par Yaya.Cout à l'aide du livre:'Programer avec python\
                     en s'amusant'"
            )
            print("")
            credit = 1

        elif nombre == "commands" and commands == 1:
            print("")
            print("Vous avez déja visionné les commands")
            print(
                'taper "credit" pour visionner les crédits;\
                taper "novelle partie" pour commancer une novelle partie;\
                     taper "quitter" pour quitter; taper commands pour voir\
                          les commandes'
            )
            print("")

        elif nombre == "commands":
            print("")
            print(
                'taper "credit" pour visionner les crédits;\
                taper "novelle partie" pour commancer une novelle partie;\
                     taper "quitter" pour quitter; taper commands pour voir\
                          les commandes'
            )
            commands = 1
            print("")

        elif nombre == "nouvelle partie":
            print("Le nombre etait: " + str(secret))
            print("Vous avez " + str(point) + " point" + ("" if point < 2 else "s"))
            dificulte = input("Quel est ton niveau de dificulté:")
            secret = random.randint(1, int(dificulte))

        elif nombre == "quitter":
            print("Le nombre etait: " + str(secret))
            print("Vous avez " + str(point) + " point" + ("" if point < 2 else "s"))
            break

        elif secret == int(nombre):
            print("Bravo")
            point = point + 5
            print("Vous avez " + str(point) + " point" + ("" if point < 2 else "s"))
            rejouer = input(
                "Veux tu rejouer ? Tape pour rejouer pour rejouer,tape autre\
                     chose pour arreter."
            )
            if rejouer == "rejouer":
                dificulte = input("Quel est ton niveau de dificulté:")
                secret = random.randint(1, int(dificulte))
                if Erreur > 8:
                    Erreur = 16
                elif Erreur >= 5:
                    Erreur = 13

        elif Erreur == 1 and point <= 1:
            print("Vous avez perdu! Le nombre etait: " + str(secret))
            print("Vous avez " + str(point) + " point" + ("" if point < 2 else "s"))
            rejouer = input(
                "Veux tu rejouer ? Tape pour rejouer pour rejouer,tape autre\
                     chose pour arreter."
            )
            dificulte = input("Quel est ton niveau de dificulté:")
            secret = random.randint(1, int(dificulte))
            #                nombre = input("Quel est ton nombre: ")
            Erreur = 11
            secret = random.randint(1, int(dificulte))

        elif Erreur == 1:
            point = point - 2
            print("Vous avez perdu! Le nombre etait: " + str(secret))
            print("Vous avez " + str(point) + " point" + ("" if point < 2 else "s"))
            rejouer = input(
                "Veux tu rejouer ? Tape pour rejouer pour rejouer,tape autre \
                    chose pour arreter."
            )
            dificulte = input("Quel est ton niveau de dificulté:")
            secret = random.randint(1, int(dificulte))
            #                nombre = input("Quel est ton nombre: ")
            Erreur = 11

        #        if secret == int(nombre):
        #                print("Correct")
        elif secret > int(nombre):
            print("Trop petit")
            Erreur = Erreur - 1
            print("Il vous reste " + str(Erreur) + " essais")
        else:
            print("Trop grand")
            Erreur = Erreur - 1
            print("Il vous reste " + str(Erreur) + " essais")

    """
                    if rejouer == "rejouer" or "azerty" or "Yaya.Cout":

                        Erreur=11
                        dificulte = input("Quel est ton niveau de dificulté:")
                        secret = random.randint(1,int(dificulte))
                        if Erreur>8:
                            Erreur=16
                        elif Erreur>=5:
                            Erreur=13
                    else:
                        break

                        or "azerty" or "Yaya.Cout"
    """


if __name__ == "__main__":
    main()
