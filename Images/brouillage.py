def main():
    from PIL import Image
    import random
    import os

    def nom_fichier():
        existance = True
        nom = "/home/neo/b Python/Images/out/out.png"
        nombre = 1
        if os.path.isfile(nom):
            pass
        else:
            return nom
        while existance:
            nom = '/home/neo/b Python/Images/out/out(' + str(nombre) + ').png'
            if os.path.isfile(nom):
                nombre += 1
            else:
                return nom
    image_open = "none"
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
    colonne, ligne = img.size
    print(colonne)
    print(ligne)

    r = random.randint(1, 255)
    v = random.randint(1, 255)
    b = random.randint(1, 255)

    img.putpixel((200, 150), (r, v, b))
    x = random.randint(1, 400)
    y = random.randint(1, 300)
    print(x)
    print(y)

    r = random.randint(1, 255)
    v = random.randint(1, 255)
    b = random.randint(1, 255)
    print("R : " + str(r))
    print("V : " + str(v))
    print("B : " + str(b))

    pixel = img.getpixel((24, 54))
    print(pixel)

    print(x)
    print(y)
    for i in range(int(ligne/2)):
        for j in range(int(colonne/2)):
            x = random.randint(0, colonne-1)
            y = random.randint(0, ligne-1)
            r = random.randint(1, 255)
            v = random.randint(1, 255)
            b = random.randint(1, 255)
            img.putpixel((x, y), (r, v, b))
    img.show()
    img.save(nom_fichier())


if __name__ == "__main__":
    main()
