def main():
    jouer = True
    totalbon = 0
    print("N'écriver qu'un un seul mot par ligne, en minuscule et sans acents")

    def verifier(bon1=None, bon2=None, bon3=None, bon4=None, bon5=None):
        if entre == bon1:
            global totalbon
            print("Bonne réponse")
            bon = "bon"

        elif entre == bon2:
            print("Bonne réponse")
            bon = "bon"

        elif entre == bon3:
            print("Bonne réponse")
            bon = "bon"

        else:
            print("Mauvaise réponse")
            bon = ""

        if bon == "bon":
            totalbon = totalbon + 1

    while jouer:
        entre = input("Comment les hommes se nourissaient-ils ? 1/3 ")
        verifier("cueillette", "chasse", "peche")
        entre = input("Comment les hommes se nourissaient-ils ? 2/3 ")
        verifier("cueillette", "chasse", "peche")
        entre = input("Comment les hommes se nourissaient-ils ? 3/3 ")
        verifier("cueillette", "chasse", "peche")

        entre = input("Où habitaient-ils ? 1/2 ")
        verifier("abri sous roche", "hutte en os")
        entre = input("Où habitaient-ils ? 2/2 ")
        verifier("abri sous roche", "hutte en os")

        entre = input("Que fabriquaient-ils ? (Grandes catégories) 1/2 ")
        verifier("statuettes", "outils")
        entre = input("Que fabriquaient-ils ? (Grandes catégories) 2/2 ")
        verifier("statuettes", "outils")

        entre = input("Que fabriquaient-ils ? (Outils) 1/5 ")
        verifier("silex", "biface", "hachereau", "propulseur", "harpon")
        entre = input("Que fabriquaient-ils ? (Outils) 2/5 ")
        verifier("silex", "biface", "hachereau", "propulseur", "harpon")
        entre = input("Que fabriquaient-ils ? (Outils) 3/5 ")
        verifier("silex", "biface", "hachereau", "propulseur", "harpon")
        entre = input("Que fabriquaient-ils ? (Outils) 4/5 ")
        verifier("silex", "biface", "hachereau", "propulseur", "harpon")
        entre = input("Que fabriquaient-ils ? (Outils) 5/5 ")
        verifier("silex", "biface", "hachereau", "propulseur", "harpon")

        s = "" if totalbon < 2 else "s"
        print("Vous avez " + str(totalbon) + " bonne" + s + " réponse" + s + " sur 10")


if __name__ == "__main__":
    main()
