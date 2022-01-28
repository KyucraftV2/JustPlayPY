from _class_xx import *
from def_armes_classexx import *

class_dic = {'1': archer,
            '2':arbaletrier,
            '3':berserker,
            '4':chevalier,               
            '5':cavalier,
            '6':batisseur}


nom_1 ='marty' #input("Nom Joueur 1:")
nom_2 ='lol' #input("Nom joueur 2:")


while nom_2 == nom_1:
    print("Ne choissisez pas deux fois le même nom !")
    nom_2 = input("Nom joueur 2:")

print(r"""
0. red 
1. blue
2. green
3. yellow         
4. purple 
5. pink
""")
print(r"""
1. Archer
2. Archer Lourd
3. Berserker 
4. Chevalier
5. Cavalier
""")
#nb_joueures = int(input('nombre de joueurs'))
nb_joueures = 2
j = []
for i in range(nb_joueures):
    ju = Joueur(f'nom_+{i}',1,1,0,0)
    j.append(ju)
    player.color.append(i)
print(batisseur)

LARGEUR = 500
HAUTEUR = 500
mazp = Map(500, 500, 20)
jeu = Game(500, 500, mazp, j)
print(f"Le joueur {player.color[1]} est {nom_2} et le {player.color[0]} est {nom_1}")
jeu.creation(LARGEUR, HAUTEUR)
