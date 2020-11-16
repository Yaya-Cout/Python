def main():
    while True:
        nombre = input("Quel est ton nombre ? ")
        nombre = int(nombre)
        david = nombre - 3
        pierre = david + 15
        henri = 123 - (david + pierre)
        print("david = " + str(nombre) + " - 3 = " + str(david))
        print("pierre = " + str(david) + " + 15 = " + str(pierre))
        if david + 3 == henri:
            print("henri = " + str(david) + " + 3 = " + str(henri))
            print("Vrai")

        else:
            print("Faux")


if __name__ == "__main__":
    main()
