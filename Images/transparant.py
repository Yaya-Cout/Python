def main():
    import argparse
    import os

    import PIL
    from PIL import Image

    def transparant(rc, gc, bc):
        colonne, ligne = img.size
        for c in range(colonne):
            for line in range(ligne):
                pixel = img.getpixel((c, line))
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                if r == rc:
                    if g == gc:
                        if b == bc:
                            img.putpixel((c, line), (255, 255, 255, 0))

    def nom_fichier():
        existance = True
        nom = "/home/neo/b Python/Images/out/out.png"
        nombre = 1
        if os.path.isfile(nom):
            pass
        else:
            return nom
        while existance:
            nom = "/home/neo/b Python/Images/out/out(" + str(nombre) + ").png"
            if os.path.isfile(nom):
                nombre += 1
            else:
                return nom

    parser = argparse.ArgumentParser()
    parser.add_argument("--Image", default="none", help="Choisir l'image")
    parser.add_argument(
        "--R", default="none", help="Choisir la couleur rouge à enlever"
    )
    parser.add_argument(
        "--V", default="none", help="Choisir la couleur verte à enlever"
    )
    parser.add_argument("--B", default="none", help="Choisir la couleur bleu à enlever")
    args = parser.parse_args()
    image_open = args.Image
    R = args.R
    V = args.V
    B = args.B
    try:
        img = Image.open(image_open)
    except IOError:
        try:
            selectfile = 'zenity --file-selection --title="Veillez\
                 séléctioner une image"'
            image_open = os.popen(selectfile).read()
            image_open = image_open.replace("\n", "")
            img = Image.open(image_open)
        except PIL.UnidentifiedImageError:
            print("Erreur lors de l'ouverture du fichier")
    print(
        "Nom : "
        + image_open
        + " Format : "
        + img.format
        + " Résolution : %dx%d" % img.size
        + " Mode d'image : "
        + img.mode
    )
    selectcolor = 'zenity --color-selection --title="Veillez séléctioner une\
         couleur"'
    color = os.popen(selectcolor).read()
    color = color.replace("\n", "")
    if "rgba" in color:
        color = color.replace("rgba(", "")
        color = color.replace(")", "")
        R, V, B, A = color.split(",")
        print("R : " + str(R) + " V : " + str(V) + " B : " + str(B) + " A : " + str(A))
        R = int(R)
        V = int(V)
        B = int(B)
        A = int(A)
    else:
        color = color.replace("rgb(", "")
        color = color.replace(")", "")
        R, V, B = color.split(",")
        print("R : " + str(R) + " V : " + str(V) + " B : " + str(B))
        R = int(R)
        V = int(V)
        B = int(B)
    print(img.getpixel((0, 0)))
    img.mode = "RGBA"
    if img.mode != "RGBA":
        # img.mode = 'RGBA'
        img.convert("RGBA")

    # transparant(0,0,0)
    # transparant(255,255,255)
    transparant(R, V, B)

    img.show()
    img.save(nom_fichier())


if __name__ == "__main__":
    main()
