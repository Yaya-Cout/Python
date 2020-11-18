def main():
    # 5*15/100
    # =5 pourcents de 15
    retour = 0
    pourcentage = 0
    nombre = input("Sur combient de nombres veut-tu le pourcentage? ")
    while True:
        if retour < 100:
            try:
                nombre = int(nombre)
            except ValueError:
                print("Et la, c'est le bug!")
                nombre = input(
                    "Sur combient de nombres veut-tu le pourcentage? ")
                retour = 0
                pourcentage = 0
                continue
            retour = pourcentage * float(nombre) / 100
            retour = retour * nombre
            print(retour)
            pourcentage = pourcentage + 1

        else:
            nombre = input("Sur combient de nombres veut-tu le pourcentage? ")
            retour = 0
            pourcentage = 0


if __name__ == "__main__":
    main()
