def main():
    # import random
    import partage

    def affiche_points():
        print("Vous avez " + str(points) + " point" + ("" if points < 2 else "s"))

    """
        def tire_deux_nombres(m):
                a = random.randint(1, m)
                b = random.randint(1, m)
                p = max(a,b)
                d = min(a,b)
                return (p, d)
        """

    # premier = random.randint(1,10)
    # deuxieme = random.randint(1,10)
    maximum = 10
    premier, deuxieme = partage.tire_deux_nombres(maximum)
    Erreur = 1
    points = 0

    while True:
        nombre = input(str(premier) + "×" + str(deuxieme) + "=")
        if (premier) * (deuxieme) == int(nombre):
            print("Bravo")
            premier, deuxieme = partage.tire_deux_nombres(maximum)
            #        premier = random.randint(1,10)
            #        deuxieme = random.randint(1,10)
            Erreur = 1
            points = points + 1
            #        if points <2:
            #            pluriel = ""
            #        else:
            #            pluriel = "s"
            #        print("Vous avez "+str(points)+" point" + pluriel)
            affiche_points()
        #        break

        elif Erreur == 2 and points < 0.5:
            resultat = premier * deuxieme
            print("Vous avez perdu! Le résultat etait: " + str(resultat))
            #        a=random.randint(1,100)
            #        b = random.randint(1,100)
            #        premier = max(a,b)
            #        deuxieme = min(a,b)
            premier, deuxieme = partage.tire_deux_nombres(maximum)
            Erreur = 1
            # print("Vous avez "+str(points)+" point" + ("" if points<2 else\
            #  "s"))
            affiche_points()

        elif Erreur == 2:
            resultat = premier * deuxieme
            print("Vous avez perdu! Le résultat etait: " + str(resultat))
            #        a=random.randint(1,100)
            #        b = random.randint(1,100)
            #        premier = max(a,b)
            #        deuxieme = min(a,b)
            premier, deuxieme = partage.tire_deux_nombres(maximum)
            Erreur = 1
            points = points - 0.5
            # print("Vous avez "+str(points)+" point" + ("" if points<2 else\
            #  "s"))
            affiche_points()
        else:
            print("Erreur")
            Erreur = Erreur + 1


if __name__ == "__main__":
    main()
