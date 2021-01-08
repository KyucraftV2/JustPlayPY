from map import * 
import time
class player:
    tablo_player = []
    color = []
    def __init__(self,nom,classe,x,y): #initialiseur
        self.classe = ClasseJ
        self._pv = classe._basepv #attribut public
        self.x = x #coordonnées du personnage
        self.y = y
        self.nom = nom 
        Map.mapa[self.nom] = self.x*10,self.y*10#rentre les coordonnées du joueurs dans mapa
        Map.prenom.append(self.nom)
        player.tablo_player.append(self)
        Game.canva.bind_all('<space>',self.attak)


    def get_pv(self): #permet de recuperer les pv pour l'affichage
        return self._pv

    def set_pv(self, val): #permet de set les pv quand on va se faire taper
        self._pv += val

    pv = property(get_pv, set_pv) 

    def attak(self,event):  #change place dans tableau--> PB
        if Game.tour >= 4:
            Game.marty.check_change()
            player.tablo_player.append(player.tablo_player[0])
            player.tablo_player.pop(0)            
            Game.tour = 0
        player.tablo_player[0].attaquer(player.tablo_player[1])
        Game.tour+= 1
        print(Game.tour)
        

    def caillou_verif(self):
        trajex = Game.canva.create_line(Map.mapa[Map.prenom[0]][0]+5,Map.mapa[Map.prenom[0]][1]+5  ,Map.mapa[Map.prenom[1]][0]+5  ,Map.mapa[Map.prenom[1]][1]+5 ,fill="red" )#creer un segment entre les deux joueurs
        traj = list(Game.canva.find_overlapping(Game.canva.coords(trajex)[0],Game.canva.coords(trajex)[1] ,Game.canva.coords(trajex)[2] ,Game.canva.coords(trajex)[3]))#regarde tous les items dans le périmetre 
        #entre les deux joueurs

        traj = list(filter(lambda x: (x>2) and (x<23),traj))#1 et deux sont les deux joueurs , de 3 23 ce sont lesz obstacles , et de 24 a 124 ce sont les lignes du tableau 
        for i in range(len(traj)):#fait pour tous les obstacles dans le périmetre
            obstacl_traj = list(Game.canva.find_overlapping(Map.obstacle_dic[traj[i]-3][0],Map.obstacle_dic[traj[i]-3][1],Map.obstacle_dic[traj[i]-3][0]+10,Map.obstacle_dic[traj[i]-3][1]+10))
            #regarde si un item passe sur l obstacle , le -3 est parsque le dico commence a 0 et que les items.obstacles commencent a 3 
            #items.canva   1-2=joueurs , 3-23 obstacles , 24-124 lignes du plateau

            if obstacl_traj[-1] > 124:#si l item a pour id +124 il est un TRAJEX
                #Pour tous x ayant un id > 124 dans le canva ,id sera supprimé car un TRAJEX
                Game.canva.delete(list(filter(lambda x: x>124,list(Game.canva.find_all()))))
                return True

        Game.canva.delete(list(filter(lambda x: x>124,list(Game.canva.find_all()))))
        #Pour tous x ayant un id > 124 dans le canva ,id sera supprimé car un TRAJEX
        return False

    def attaquer(self,adv):
        touché_caillou = self.caillou_verif()
        if touché_caillou == False:
            adv.set_pv(-5)

        advpv = adv.get_pv()
        selfpv = self.get_pv()

        if (advpv < 0) or (selfpv<0):
            print(f'{player.tablo_player[0].nom} a gagné')
            Game.fenetre.destroy()

        print(f'joueur : {self.nom}, pv : {self.pv}')
        print(f'joueur : {adv.nom}, pv : {adv.pv}')
        
        score_player_1=Label(Game.fenetre, text=f'{player.tablo_player[0].nom}', bg=Game.color_tablo[player.color[0]]) 
        score_player_1.pack()

        

class ClasseJ:

    def __init__(self,basepv,arme,baseforce): #initialiseur
        self._basepv=basepv
        self.arme = arme
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
    fenetre = tk.Tk()
    canva = tk.Canvas(fenetre, width=500+10, height=500+10)
    color_tablo=["red", "blue","green","yellow","purple","pink"]
    tour = 0
    marty = 0
    i = 0
    def __init__(self, largeur, hauteur, maap, p1, p2):
        self.largeur = largeur
        self.hauteur = hauteur
        self.maap = maap
        self.p1 = p1
        self.p2 = p2
        Game.marty = self 
    
    def droite(self,event):  #fonction pour bouger
        self.bouger(10,0)

    def gauche(self,event):
        self.bouger(-10,0)

    def haut(self,event):
        self.bouger(0,-10)

    def bas(self,event):
        self.bouger(0,10)
    
    def check_change(self):
        if Game.tour >= 4:
            Game.i += 1
            Map.trouv.append(Map.trouv[0])
            Map.trouv.pop(0)
            Map.prenom.append(Map.prenom[0])
            Map.prenom.pop(0)
            Game.tour = 0
        if Game.i%2 == 0:
            Game.fenetre.configure(bg=Game.color_tablo[player.color[0]])
        else : 
            Game.fenetre.configure(bg=Game.color_tablo[player.color[1]])

    def bouger(self,dx,dy):

        self.check_change()
        
        Game.canva.pack()
        #collision border

        Map.mapa[Map.prenom[0]]=Map.mapa[Map.prenom[0]][0] + dx ,Map.mapa[Map.prenom[0]][1] + dy
        if (Map.mapa[Map.prenom[0]][0] > 500) or (Map.mapa[Map.prenom[0]][1] > 500) or (Map.mapa[Map.prenom[0]][0]< 0) or (Map.mapa[Map.prenom[0]][1]< 0):
            Map.mapa[Map.prenom[0]]=Map.mapa[Map.prenom[0]][0] - dx ,Map.mapa[Map.prenom[0]][1] - dy
        else:
            Game.canva.move(Map.trouv[0],dx,dy)
        
        caillou_collision_player = list(Game.canva.find_overlapping(Map.mapa[Map.prenom[0]][0]+4,Map.mapa[Map.prenom[0]][1]+4 ,Map.mapa[Map.prenom[0]][0]+6 ,Map.mapa[Map.prenom[0]][1]+6))
        caillou_collision_player = list(filter(lambda x: (x>2) and (x<23),caillou_collision_player))
        if caillou_collision_player != []:
            Map.mapa[Map.prenom[0]]=Map.mapa[Map.prenom[0]][0] - dx ,Map.mapa[Map.prenom[0]][1] - dy
            Game.canva.move(Map.trouv[0],-dx,-dy)
        
        Game.tour+=1
                

        
    def creation(self, largeur, hauteur):
        Game.fenetre.geometry('%sx%s'%(self.largeur+50,self.hauteur+50))
        Game.canva.pack()
        i=0
        for key in Map.mapa:#si dans mapa il y a un str alor le faire en bleue car c est un joueur
        
            Map.trouv.append(Game.canva.create_rectangle(Map.mapa[key][0],Map.mapa[key][1],Map.mapa[key][0]+10,Map.mapa[key][1]+10,fill=Game.color_tablo[player.color[i]]))
            i+=1

        for i in range(len(Map.obstacle_dic)):
            Game.canva.create_rectangle(Map.obstacle_dic[i][0],Map.obstacle_dic[i][1],Map.obstacle_dic[i][0]+10,Map.obstacle_dic[i][1]+10,fill="black")

        
        for i in range(round(self.largeur/10)+1):
            Game.canva.create_line(i*10 ,0  ,i*10  ,self.largeur+10 , fill="grey")#colonnes

        for i in range(round(self.largeur/10)+1):
            Game.canva.create_line(0 , i*10 , self.largeur +10, i*10 , fill="grey")#lignes     


        Game.fenetre.configure(bg=Game.color_tablo[player.color[0]])
        Bouton_Quitter=Button(Game.fenetre, text ='Quitter', command = Game.fenetre.destroy)#boutton pour quitter le jeu
        Bouton_Quitter.pack()


        Game.canva.bind_all('<Right>', self.droite)#fleches directionnelles pour les events
        Game.canva.bind_all('<Left>', self.gauche)
        Game.canva.bind_all('<Up>', self.haut)
        Game.canva.bind_all('<Down>', self.bas)
        Game.canva.bind_all('<space>',)
        
        Game.fenetre.mainloop()#affiche le canva
