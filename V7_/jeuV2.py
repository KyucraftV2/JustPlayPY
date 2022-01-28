from _class_ import *
from def_armes_classe import *

class_dic = {'1': archer,
            '2':arbaletrier,
            '3':berserker,
            '4':chevalier,               
            '5':cavalier}


nom_j1 ='marty' #input("Nom Joueur 1:")
nom_j2 ='lol' #input("Nom joueur 2:")
nom_j3 ='lodddl' #input("Nom joueur 2:")

while nom_j2 == nom_j1:
    print("Ne choissisez pas deux fois le même nom !")
    nom_j2 = input("Nom joueur 2:")

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
    ju = player(f'nom_{i}', class_dic[str(i+1)],5+i*2,5+i*2)
    j.append(ju)
    player.color.append(0)

pa = (50,50)

print(class_dic)
LARGEUR = 500
HAUTEUR = 500
mazp = Map(500, 500, 20)
jeu = Game(500, 500, mazp, j,pa)
print(f"Le joueur {player.color[1]} est {nom_j2} et le {player.color[0]} est {nom_j1}")
jeu.creation(LARGEUR, HAUTEUR)
