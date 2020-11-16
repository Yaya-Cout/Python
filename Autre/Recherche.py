def main():
    import webbrowser
    recherche = 0
    recherche2 = 0
    while True:
        if recherche < 10:
            recherche = recherche + 1
            recherche2 = recherche2 + 1
            adresse = input("Quel adresse veut-tu ouvrir ? ")
            adresse = "https://www.ecosia.org/search?q=" + adresse
            webbrowser.open(adresse)
        else:
            print("Vous avez fait " + str(recherche2) + " recherches.")
            recherche = 0


if __name__ == "__main__":
    main()
