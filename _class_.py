class player:

    def __init__(self,classe,coords):
        self.classe = ClasseJ
        self._pv = classe._basepv #attribut public
        self.coords = coords

    def get_pv(self): #permet de recuperer les pv
        return self._pv

    def set_pv(self, val): #permet de set les pv quand on va se faire taper
        self._pv += val

    pv = property(get_pv, set_pv) 



class ClasseJ:

    def __init__(self,basepv,arme,baseforce):
        self._basepv=basepv
        self.arme = Arme
        self.baseforce = baseforce


class Arme:

    def __init__(self,nom,degats,portee):
        self._nom = nom
        self._degats = degats
        self.portee = portee

    def get_nom(self):  #pour recup le nom de l'arme
        return self._nom

    def set_nom(self, val):  #pour set le nom de l'arme si jamais
        self._nom = val

    nom=property(get_nom, set_nom)


    def get_degats(self):  #pour savoir combien l'arme fait
        return self._degats

    def set_degats(self,val):  #changer les degats de l'arme si jamais
        self._degats = val

    degats = property(get_degats,set_degats)

