from _class_ import *
from def_armes_classe import *

nom_j1 = input("Nom Joueur 1:")
nom_j2 = input("Nom joueur 2:")

j1 = player(nom_j1, Archer,18,18)
j2 = player(nom_j2, Cavalier, 22, 22)
LARGEUR = 500
HAUTEUR = 500
mazp = Map(500, 500, 20)
jeu = Game(500, 500, mazp, j1, j2)
jeu.creation(LARGEUR, HAUTEUR)
