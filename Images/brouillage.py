def main():
    # colonne,ligne=img.size
    # print(colonne)
    # print(ligne)
    ##
    # pixel=img.getpixel((24,54))
    # print(pixel)
    ##
    # r=random.randint(1,255)
    # v=random.randint(1,255)
    # b=random.randint(1,255)
    # print(r)
    # print(v)
    # print(b)
    ##
    # img.putpixel((200,150),(r,v,b))
    # x=random.randint(1,400)
    # y=random.randint(1,300)
    # print(x)
    # print(y)

    # r=random.randint(1,255)
    # v=random.randint(1,255)
    # b=random.randint(1,255)
    # #print("R : " + str(r))
    # #print("V : " + str(v))
    # #print("B : " + str(b))

    # pixel=img.getpixel((24,54))
    # print(pixel)

    # x=random.randint(1,400)
    # y=random.randint(1,300)
    # print(x)
    # print(y)
    # for i in range(ligne):
    # img.putpixel((x,i),(r,v,b))
    # for j in range(colonne):
    # img.putpixel((j,y),(v,b,r))

    # img.putpixel((200,150),(255,0,0))

    import os
    import random

    from PIL import Image

    image_open = "file"
    try:
        img = Image.open(image_open)
    except IOError:
        try:
            selectfile = 'zenity --file-selection \
                --title="Veillez séléctioner une image"'
            image_open = os.popen(selectfile).read()
            image_open = image_open.replace("\n", "")
            img = Image.open(image_open)
        except IOError:
            print("Erreur d'ouverture du fichier")
    print(
        "Nom : "
        + image_open
        + " Format : "
        + img.format
        + " Résolution : %d×%d" % img.size
        + " Mode d'image : "
        + img.mode
    )
    colonne, ligne = img.size
    total_pixels = ligne * colonne
    nombre_tour = random.randint(0, total_pixels / 2)
    tours_faits = 0
    while True:
        x = random.randint(0, colonne - 1)
        y = random.randint(0, ligne - 1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        position = (x, y)
        color = (r, g, b)
        img.putpixel(position, color)
        tours_faits += 1
        if tours_faits == nombre_tour:
            break
    img.show()


if __name__ == "__main__":
    main()
