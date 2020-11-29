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
0. red 
1. blue
2. black
3. green
4. yellow 
5. purple 
6. pink
""")


player.color.append(int(input("Couleur Joueur 1:")))
player.color.append(int(input("Couleur Joueur 2:")))


while player.color[1] == player.color[0]:
    print("Ne choissisez pas deux fois la même couleur !")
    player.color[1]= int(input("Couleur Joueur 2:"))


print(r"""
1. Archer
2. Archer Lourd
3. Berserker 
4. Chevalier
5. Cavalier
""")

while class_correct == False:
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
print(f"Le joueur {player.color[1]} est {nom_j2} et le {player.color[0]} est {nom_j1}")
jeu.creation(LARGEUR, HAUTEUR)
