def main():
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
            secret = random.randint(1, int(dificulte))

        elif secret > nb:
            print("Trop petit")

        elif str(secret) < nombre:
            print("Trop grand")


if __name__ == "__main__":
    main()
