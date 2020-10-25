def main():
    while True:
        nombre = input("Quel nombre veut-tu convretir en binaire? ")
        nombre = int(nombre)
        nombre = bin(nombre)
        print(nombre)


if __name__ == "__main__":
    main()
