#!/bin/python3
# -*- coding: utf-8 -*-
import tkinter


def main():
    fenetre = tkinter.Tk()

    # Couleur de fond
    fenetre['bg'] = 'white'

    label = tkinter.Label(fenetre, text="Hello World")
    label.pack()

    # bouton de sortie
    bouton = tkinter.Button(fenetre, text="Fermer", command=fenetre.quit)
    bouton.pack()

    # Label
    label = tkinter.Label(fenetre, text="Input :", bg="yellow")
    label.pack()

    # Entrée
    string = ""
    value = tkinter.StringVar()
    value.set("Blabla")
    entree = tkinter.Entry(fenetre, textvariable=string, width=30)
    entree.pack()

    # Checkbutton
    bouton = tkinter.Checkbutton(fenetre, text="Nouveau ?")
    bouton.pack()

    # Radiobutton
    value = tkinter.StringVar()
    bouton1 = tkinter.Radiobutton(fenetre, text="Oui", variable=value, value=1)
    bouton2 = tkinter.Radiobutton(fenetre, text="Non", variable=value, value=2)
    bouton3 = tkinter.Radiobutton(
        fenetre, text="Peut être", variable=value, value=3)
    bouton1.pack()
    bouton2.pack()
    bouton3.pack()

    # Liste
    liste = tkinter.Listbox(fenetre)
    liste.insert(1, "Python")
    liste.insert(2, "PHP")
    liste.insert(3, "jQuery")
    liste.insert(4, "CSS")
    liste.insert(5, "Javascript")
    liste.pack()

    # Canvas
    canvas = tkinter.Canvas(
        fenetre, width=150, height=120, background='yellow')
    # ligne1 = canvas.create_line(75, 0, 75, 120)
    # ligne2 = canvas.create_line(0, 60, 150, 60)
    # txt = canvas.create_text(75, 60, text="Cible",
    #                          font="Arial 16 italic", fill="blue")
    # Vous pouvez créer d'autres éléments:

    # create_arc():  arc de cercle
    # create_bitmap():  bitmap
    # create_image():  image
    # create_line():  ligne
    # create_oval():  ovale
    # create_polygon():  polygone
    # create_rectangle():  rectangle
    # create_text():  texte
    # create_window():  fenetre
    # canvas.coords(élément, x0, y0, x1, y1)
    # canvas.delete(élément)
    # # print(dir(Canvas()))

    canvas.pack()

    # Scale
    value = tkinter.DoubleVar()
    scale = tkinter.Scale(fenetre, variable=value)
    scale.pack()

    # Frames
    # frame 1
    Frame1 = tkinter.Frame(fenetre, borderwidth=2, relief=tkinter.GROOVE)
    Frame1.pack(side=tkinter.LEFT, padx=30, pady=30)

    # frame 2
    Frame2 = tkinter.Frame(fenetre, borderwidth=2, relief=tkinter.GROOVE)
    Frame2.pack(side=tkinter.LEFT, padx=10, pady=10)

    # frame 3 dans frame 2
    Frame3 = tkinter.Frame(
        Frame2, bg="white", borderwidth=2, relief=tkinter.GROOVE)
    Frame3.pack(side=tkinter.RIGHT, padx=5, pady=5)

    # Ajout de labels
    tkinter.Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
    tkinter.Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
    tkinter.Label(Frame3, text="Frame 3", bg="white").pack(padx=10, pady=10)

    fenetre.mainloop()

    print(string)
    print(value)
    print(dir(fenetre))


if __name__ == "__main__":
    main()
