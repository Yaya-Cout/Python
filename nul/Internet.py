def main():
    import webbrowser
    recherche = 0

    while True:
        if recherche < 2:
            recherche = recherche + 1
            adresse = input("Quel adresse veut-tu ouvrir")
            webbrowser.open(adresse)
        else:
            print("Vous avez fait " + str(recherche) + " recherches.")
            recherche = recherche + 1
            adresse = input("Quel adresse veut-tu ouvrir")
            webbrowser.open(adresse)


if __name__ == "__main__":
    main()
