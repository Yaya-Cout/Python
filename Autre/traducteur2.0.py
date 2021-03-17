def main():
    bonjour = "Salut tout le monde"
    le_monde = "appuie sur 1 ou 2"
    print(bonjour + " " + le_monde)

    test = input()
    """
    bonjour='Salut tout le monde'
    le_monde='appuie sur espace'
    print( bonjour + ' ' +le_monde)
    """
    print(test)

    caractere = ""
    if test == "1":
        caractere = "a"
    elif test == "2":
        caractere = "b"
    else:
        caractere = "ERR"
    print(caractere)

    print("Dictionnaire")
    dico = {"a": 1, "b": 2, "y": 25, "z": 0}

    chaine = "abzy"
    total = 0
    for c in chaine:
        print(c)
        print(dico[c])
        total = total + dico[c]
    print("total: " + str(total))
    """
    if test == '2':
        1=a
        2=b
        3=c
        4=d
        5=e
        6=f
        7=g
        8=h
        9=i
        10=j
        11=k
        12=l
        13=m
        14=n
        15=o
        16=p
        17=q
        18=r
        19=s
        20=t
        21=u
        22=v
        23=w
        24=x
        25=y
        0=z

    """


if __name__ == "__main__":
    main()
