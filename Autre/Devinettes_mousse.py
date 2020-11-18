def main():
    import random
    Erreur = 10
    rejouer = "rejouer"
    point = 0
    print("Bienvenue dans ce jeu de devinette")
    dificulte = input("Quel est ton niveau de dificulté:")

    secret = random.randint(1, int(dificulte))
    while rejouer == "rejouer":
        nombre = input("Quel est ton nombre: ")
        try:
            nb = int(nombre)
        except ValueError:
            print("\n\t Et la, c'est le bug!\n")
            continue

        if secret == nb:
            print("Bravo")
            point = point+5
            print("Vous avez "+str(point)+" point"+("" if point < 2 else "s"))
            rejouer = input(
                "Veux tu rejouer ? Tape pour rejouer pour rejouer,tape autre\
                     chose pour arreter.")
            if rejouer == "1":
                Erreur = 10
            elif rejouer == "2":
                dificulte = input("Quel est ton niveau de dificulté:")
                secret = random.randint(1, int(dificulte))
                Erreur = 10

        elif Erreur == 1:
            point = point-2
            print("Vous avez perdu! Le nombre etait: "+str(secret))
            print("Vous avez "+str(point)+" point"+("" if point < 2 else "s"))
            rejouer = input(
                "Veux tu rejouer ? Tape pour rejouer pour rejouer,tape autre\
                     chose pour arreter.")
            dificulte = input("Quel est ton niveau de dificulté:")
            secret = random.randint(1, int(dificulte))

            Erreur = 11
        elif secret > nb:
            print("Trop petit")
            Erreur = Erreur-1
            print("Il vous reste " + str(Erreur)+" essais")

        elif str(secret) < nombre:
            print("Trop grand")
            Erreur = Erreur-1
            print("Il vous reste " + str(Erreur)+" essais")


if __name__ == "__main__":
    main()
