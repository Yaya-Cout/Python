#!/usr/bin/python3
def main():
    try:
        import sys

        import unidecode

        def entre(text):
            version = sys.version_info[:1]
            if version == (2,):
                result = input(text)
            elif version == (3,):
                result = input(text)
            else:
                print("Erreur de version")
            return result

        def encoder(decalage, s):
            s2 = unidecode.unidecode(s)
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            dico = {}
            inchanges = " .,!?;:/\\&\"'(-_#{[|`^@)]=}$£µ*%§<>²0123456789"
            for i in inchanges:
                dico[i] = i

            position = decalage

            for i in alphabet:
                dico[i] = alphabet[position]
                dico[i.upper()] = alphabet.upper()[position]
                position = (position + 1) % len(alphabet)

            # print(dico)

            secret = ""
            for i in s2:
                secret += dico[i]
            print(secret)

        while True:
            try:
                decalage = int(entre("Quel décalage voulez vous ? "))
            except ValueError:
                print("Veiller entrer un nombre valide.")
                continue
            s = entre("Votre mot à coder/décoder : ")

            encoder(decalage, s)
            print(s)
            encoder(decalage - 2, s)
    except ValueError:
        print("%s" % sys.exc_info()[1])


if __name__ == "__main__":
    main()
