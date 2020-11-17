class player:

    def __init(self,pv,classe,coords):
        self._pv = pv
        self.classe = ClasseJ
        self.coords = coords

    def get_pv(self):
        return self._pv

    def set_pv(self, val):
        self._pv = val

    pv = property(get_pv, set_pv) 

class ClasseJ:

    def __init__(self,basepv,arme,baseforce):
        self.basepv=basepv
        self.arme = Arme
        self.baseforce = baseforce


class Arme:

    def __init__(self,nom,degats,portee):
        self._nom = nom
        self._degats = degats
        self.portee = portee

    def get_nom(self):
        return self._nom

    def set_nom(self, val):
        self._nom = val

    nom=property(get_nom, set_nom)


    def get_degats(self):
        return self._degats

    def set_degats(self,val):
        self._degats = val

    degats = property(get_degats,set_degats)

