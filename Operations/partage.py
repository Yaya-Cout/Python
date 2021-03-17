import random

"""from partage import *"""


def tire_deux_nombres(maxi, mini=1):
    """tire_deux_nombres sert a obtenir deux nombres au hasard."""
    a = random.randint(mini, maxi)
    b = random.randint(mini, maxi)
    p = max(a, b)
    d = min(a, b)
    return (p, d)


def attendre(secondes=1, message=""):
    """attendre sert à attendre le temps demandé (par défaut le temps est 1\
         seconde) et à afficher le texte demandé(exemple: attendre(2,"test")\
              attendre va attendre 2 secondes en affichant test.)"""
    temps = 14000000 * secondes
    temps_a_attendre = 0
    print(message)
    while temps_a_attendre < temps:
        # if message == "":
        #   if temps_a_attendre < temps:
        #       temps_a_attendre = temps_a_attendre + 1
        if temps_a_attendre < temps:
            temps_a_attendre = temps_a_attendre + 1
