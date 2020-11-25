from _class_ import *

Arc = Arme('Arc', 60, 120)
Arbalete = Arme('Arbaléte', 80, 100)
Hache = Arme('Hache', 150, 20)
Epee = Arme('Epée', 100, 30)
Lance = Arme('Lance', 80, 50)


Archer = ClasseJ(120, Arc, 10)
Archer_Lourd = ClasseJ(100, Arbalete, 25)
Berserker = ClasseJ(90, Hache, 100)
Chevlier = ClasseJ(100, Epee, 70)
Cavalier=ClasseJ(110, Lance, 45)



marty = player('marty',Archer,18,18)#mettre les coordonnées entre 0 et 50 
george = player('Georges', Cavalier, 22, 22)
LARGEUR = 500
HAUTEUR = 500
mazp = Map(500, 500, 20)
jeu = Game(500, 500, mazp, marty, george)
jeu.creation(LARGEUR, HAUTEUR)
