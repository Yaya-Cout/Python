def main():
    import serial
    import unidecode

    port = "/dev/" + input("Quel port voulez-vous ? ")
    speed = int(input("Quel vitesse voulez-vous ? "))
    # port = "/dev/ttyACM0"
    # port = "/dev/rfcomm4"
    # port = "/dev/ttyUSB0"
    with serial.Serial(port, speed, timeout=10, writeTimeout=10) as port_serie:
        if port_serie.isOpen():
            mode = input(
                "Entrez un nombre (1 pour lecture,\
                     Autre chose pour écriture) : "
            )
            if mode == "1":
                while True:
                    ligne = port_serie.readline()
                    ligne = str(ligne)
                    ligne = ligne.replace("b'", "", 1)
                    ligne = ligne.replace("'", "")
                    ligne = ligne.replace("\\n", "")
                    ligne = ligne.replace("\\r", "")
                    if ligne != "":
                        print(ligne)
            else:
                while True:
                    text = input("Entrez un texte à envoyer à l'arduino : ")
                    text = unidecode.unidecode(text)
                    text += "\n"
                    port_serie.write(text.encode("ascii"))


if __name__ == "__main__":
    main()
