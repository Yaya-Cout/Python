def main():
    import PIL
    from PIL import Image
    import os
    import argparse

    def noirblanc():
        colonne, ligne = img.size
        for c in range(colonne):
            for line in range(ligne):
                pixel = img.getpixel((c, line))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                rn = int(r + g + b / 3)
                img.putpixel((c, line), (rn, rn, rn))

    def nom_fichier():
        existance = True
        nom = "/home/neo/out.png"
        nombre = 1
        if os.path.isfile(nom):
            pass
        else:
            return nom
        while existance:
            nom = '/home/neo/out(' + str(nombre) + ').png'
            if os.path.isfile(nom):
                nombre += 1
            else:
                return nom

    parser = argparse.ArgumentParser()
    parser.add_argument("--Image", default="none", help="Choisir l'image")
    args = parser.parse_args()
    image_open = args.Image
    try:
        img = Image.open(image_open)
    except IOError:
        try:
            selectfile = 'zenity --file-selection --title="Veillez séléctioner\
                 une image"'
            image_open = os.popen(selectfile).read()
            image_open = image_open.replace("\n", "")
            img = Image.open(image_open)
        except PIL.UnidentifiedImageError:
            print("Erreur lors de l'ouverture du fichier")
    print("Nom : " + image_open + " Format : " + img.format +
          " Résolution : %dx%d" % img.size + " Mode d'image : " + img.mode)
    print(img.getpixel((0, 0)))
    noirblanc()

    img.show()
    img.save(nom_fichier())


if __name__ == "__main__":
    main()
