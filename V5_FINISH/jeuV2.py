from _class_ import *
from def_armes_classe import *

class_correct = False 
class_dic = {'1': archer,
            '2': archer_Lourd,
            '3':berserker,
            '4':chevalier,
            '5':chevalier}

def check_class(class_type):
    check = True
    try:
        travel = class_dic[class_type]
    except KeyError:
        print("Classe Inconnu")
        check = False
    return check


nom_j1 = input("Nom Joueur 1:")
nom_j2 = input("Nom joueur 2:")
while nom_j2 == nom_j1:
    print("Ne choissisez pas deux fois le même nom !")
    nom_j2 = input("Nom joueur 2:")


print(r"""
1. Archer
2. Archer Lourd
3. Berserker 
4. Chevalier
5. Cavalier
""")

while class_correct == False:
    print("ATTENTION A NE PAS METTRE DE MAJUSCULE QUANT TU CHOISI TA CLASSE")
    class_type1 = input("Classe Joueur 1:")
    class_type2 = input("Classe Joueur 2:")
    if check_class(class_type1) == True and check_class(class_type2) == True:
        class_correct = True 


j1 = player(nom_j1, class_dic[class_type1],18,18)
j2 = player(nom_j2, class_dic[class_type2], 22, 22)
LARGEUR = 500
HAUTEUR = 500
mazp = Map(500, 500, 20)
jeu = Game(500, 500, mazp, j1, j2)
print(f"Le joueur rouge est {nom_j1} et le bleu est {nom_j2}")
jeu.creation(LARGEUR, HAUTEUR)
