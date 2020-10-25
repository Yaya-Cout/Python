# !/usr/bin/python
def main():
    import random
    secret = random.randint(0, 100)
    while True:
        nombre = input("Quel est ton nombre ? ")
        try:
            nombre = int(nombre)
        except:
            print("Veuillez entrer un nombre valide")
            continue
        if nombre < secret:
            print("Trop petit")
        elif nombre > secret:
            print("Trop grand")
        else:
            print("Bravo !")
            secret = random.randint(0, 100)


if __name__ == "__main__":
    main()
