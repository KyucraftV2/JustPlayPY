from _class_ import *

Arc = Arme('Arc', 60, 120)
Hache = Arme('Hache', 150, 20)
Epee = Arme('Epée', 100, 30)
Lance = Arme('Lance', 80, 50)


Archer = ClasseJ(120, Arc, 10)
Berserker = ClasseJ(90, Hache, 100)
Chevlier = ClasseJ(100, Epee, 70)
Cavalier=ClasseJ(110, Lance, 45)


kliklou=player(Archer, 100)

print(kliklou.get_pv())
kliklou.set_pv(20)
print(kliklou.get_pv())