def main():
    import sys
    version = sys.version_info[:1]

    def entre(text):
        if version == (2,):
            result = input(text)
        elif version == (3,):
            result = input(text)
        else:
            print("Erreur de version")
        return result

    def affichage_ligne(text):
        # if version == (2,):
        #     try:
        #         print(text),
        #     except:
        #         pass
        # elif version == (3,):
        #     try:
        #         print(text, end='')
        #     except:
        #         pass
        # else:
        #     print("Erreur de version")
        # try:
        #     print(text, end='')
        # except:
        #     print(text),
        print(text, end='')
    dico = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p',
            'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a', 'p': 'q', 'p': 'q', 'p': 'q', ' ': ' '}
    dico = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q',
            'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a', 'p': 'q', 'p': 'q', 'p': 'q', '&': 'fu', 'é': 'f', 'é': 'f', ' ': ' '}
    while True:
        text = entre("Quel est ton texte ? ")
        for c in text:
            affichage_ligne(c)
        print("")

        for c in text:
            if c in dico:
                c = dico[c]
            affichage_ligne(c)
        print("")

        for c in text:
            for loop in range(len(dico)+1):
                if c in dico:
                    c = dico[c]
            affichage_ligne(c)
        print("")


if __name__ == "__main__":
    main()
