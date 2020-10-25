def main():
    import random

    def affiche_points():
        print("Vous avez "+str(points)+" point" + ("" if points < 2 else "s"))

    points = 0
    a = random.randint(1, 100)
    # premier=
    b = random.randint(1, 100)
    premier = max(a, b)
    deuxieme = min(a, b)
    Erreur = 1
    while True:
        nombre = input(str(premier) + "+" + str(deuxieme) + "=")
        if (premier)+(deuxieme) == int(nombre):
            print("Bravo")
            premier = random.randint(1, 100)
            deuxieme = random.randint(1, 100)
            Erreur = 1
            points = points+1
            affiche_points()
    #        break

        elif Erreur == 2 and points < 0.5:
            resultat = premier+deuxieme
            print("Vous avez perdu! Le résultat etait: "+str(resultat))
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            premier = max(a, b)
            deuxieme = min(a, b)
            Erreur = 1
            points = points-0.5
            affiche_points()

        elif Erreur == 2:
            resultat = premier+deuxieme
            print("Vous avez perdu! Le résultat etait: "+str(resultat))
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            premier = max(a, b)
            deuxieme = min(a, b)
            Erreur = 1
            points = points-0.5
            affiche_points()

        else:
            print("Erreur")
            Erreur = Erreur+1


if __name__ == "__main__":
    main()
