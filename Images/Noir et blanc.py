def main():
    from PIL import Image
    import os
    import argparse

    def noirblanc():
        colonne, ligne = img.size
        for c in range(colonne):
            for l in range(ligne):
                pixel = img.getpixel((c, l))
                try:
                    r, g, b, a = pixel
                except ValueError:
                    r, g, b = pixel
                rn = int(r + g + b / 3)
                img.putpixel((c, l), (rn, rn, rn))

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
    R = args.R
    V = args.V
    B = args.B
    try:
        img = Image.open(image_open)
    except IOError:
        try:
            selectfile = 'zenity --file-selection --title="Veillez séléctioner une image"'
            image_open = os.popen(selectfile).read()
            image_open = image_open.replace("\n", "")
            img = Image.open(image_open)
        except:
            print("Erreur lors de l'ouverture du fichier")
    print("Nom : " + image_open + " Format : " + img.format +
          " Résolution : %dx%d" % img.size + " Mode d'image : " + img.mode)
    print(img.getpixel((0, 0)))
    noirblanc()

    img.show()
    img.save(nom_fichier())


if __name__ == "__main__":
    main()
