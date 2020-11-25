from _class_ import *

LARGEUR = 500
HAUTEUR = 500

arc = Arme('Arc', 60, 120)
arbalete = Arme('Arbaléte', 80, 100)
hache = Arme('Hache', 150, 20)
epee = Arme('Epée', 100, 30)
lance = Arme('Lance', 80, 50)


archer = ClasseJ(120, Arc, 10)
archer_Lourd = ClasseJ(100, Arbalete, 25)
berserker = ClasseJ(90, Hache, 100)
chevlier = ClasseJ(100, Epee, 70)
cavalier=ClasseJ(110, Lance, 45)



marty = player('marty', archer, 18, 18)#mettre les coordonnées entre 0 et 50 
george = player('george', cavalier, 22, 22)

mazp = Map(LARGEUR, HAUTEUR, 20)
jeu = Game(LARGEUR, HAUTEUR, mazp, marty, george)
jeu.creation(LARGEUR, HAUTEUR)
marty.attaquer('george')
