from _class_xx import *


arc = Arme('Archer', 60, 120)
arbalete = Arme('Arbaletrier', 80, 100)
hache = Arme('Berserker', 150, 20)
epee = Arme('Chevalier', 100, 30)
lance = Arme('Cavalier', 80, 50)
marteau = Arme('Batisseur',0,50)


archer = ClasseJ('archer',120, arc, 10)
arbaletrier = ClasseJ('arbaletrier',100, arbalete, 25)
berserker = ClasseJ('berserker',90, hache, 100)
chevalier = ClasseJ('chevalier',100, epee, 70)
cavalier=ClasseJ('cavalier',110, lance, 45)
batisseur = ClasseJ('batisseur',100,marteau,0)

caserne = Batiment(1,2000,10)
ferme = Batiment(2,1000,0)
tour = Batiment(3,500,50)

print("fdp")