from map import * 

class player:
    
    def __init__(self,nom,classe,x,y): #initialiseur
        self.classe = ClasseJ
        self._pv = classe._basepv #attribut public
        self.x = x
        self.y = y
        self.nom = nom 
        Map.mapa[self.nom] = self.x*10,self.y*10#rentre les coordonnées du joueurs dans mapa
        Map.prenom.append(self.nom)
        self._tour = 0


    def get_pv(self): #permet de recuperer les pv pour l'affichage
        return self._pv

    def set_pv(self, val): #permet de set les pv quand on va se faire taper
        self._pv += val

    def get_tour(self):
        return self._tour

    def set_tour(self, val):
        self._tour += val

    def tour_par_tour(self):
        if self.tour > 5:
            Map.prenom.append(Map.prenom[0])
            Map.prenom.pop
            Map.trouv.append(Map.trouv[0])
            Map.trouv.pop
            print(Map.prenom)
            self.tour = 0
        else : self.set_tour(1)


    tour = property(get_tour, set_tour)
    pv = property(get_pv, set_pv) 





class ClasseJ:

    def __init__(self,basepv,arme,baseforce): #initialiseur
        self._basepv=basepv
        self.arme = Arme
        self.baseforce = baseforce


class Arme:

    def __init__(self,nom,degats,portee): #initialiseur
        self._nom = nom
        self._degats = degats
        self.portee = portee

    def get_nom(self):  #pour recup le nom de l'arme pour l'affichage aussi
        return self._nom

    def set_nom(self, val):  #pour set le nom de l'arme si jamais --> si jamais on a envie de changer le nom de l'arme 
        self._nom = val

    nom=property(get_nom, set_nom)


    def get_degats(self):  #pour savoir combien l'arme fait --> va servir pour effectuer les combats
        return self._degats

    def set_degats(self,val):  #changer les degats de l'arme si jamais
        self._degats = val

    degats = property(get_degats,set_degats)




class Game:
    def __init__(self, largeur, hauteur, maap, p1, p2):
        self.largeur = largeur
        self.hauteur = hauteur
        self.maap = maap
        self.p1 = p1
        self.p2 = p2

    def droite(self,event):
        self.bouger(10,0)

    def gauche(self,event):
        self.bouger(-10,0)

    def haut(self,event):
        self.bouger(0,-10)

    def bas(self,event):
        self.bouger(0,10)

    def bouger(self,dx,dy):
        if self._tour < 5:
            self.tour_par_tour()
        else:
            self.tour_par_tour()


'''
class jouage:

    def __init__(self,nom,degats,portee): #initialiseur
    self._nom = nom
    self._degats = degats
    self.portee = portee
'''
