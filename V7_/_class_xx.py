import time
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk, Image





class player:

    color = []
    def __init__(self,classe,x,y,team): #initialiseur
        
        self.classe = ClasseJ
        self.team = team
        self._pv = classe._basepv #attribut public
        self.x = x #coordonnées du personnage
        self.y = y

        Map.joueur[Joueur.joueurs[0].nom] = self.x*10,self.y*10#rentre les coordonnées du joueurs dans joueur
        Map.prenom.append(Joueur.joueurs[0].nom)
        Joueur.set_soldats(Joueur.joueurs[0],self.classe,self,10,10)       
        #print(self.classe.appel_classe[0].id)
  
    def get_pv(self): #permet de recuperer les pv pour l'affichage
        return self._pv

    def set_pv(self, val): #permet de set les pv quand on va se faire taper
        self._pv += val

    pv = property(get_pv, set_pv) 

    def construire(self,type,coord):
        #type est le batiment , caserne , ferme ect
        #coord place ou le batiment va etre construit
        return None

    
    def attaquer(self,adv):
        #touché_caillou = self.caillou_verif()
        return None
        '''
        degats = self.classe.appel_classe.arme.appel_arme.get_degats()
        resistance = adv.classe.appel_classe.baseforce
        degats = round(degats/resistance) * 10
        #for i in range(10):
            #print(player.tablo_player[i].classe.appel_classe.arme.appel_arme.get_nom())
        
        #if touché_caillou == False:
         #   adv.set_pv(-degats)

        #advpv = adv.get_pv()
        #selfpv = self.get_pv()
        '''

class Joueur:
    joueurs = []
    def __init__(self,nom,team,soldats,batiments,ressources):
        
        #nb_soldats->dico {lancier:[x,y],chevalier:[id,id]}
        #batiments = {caserne:[x,y],ferme:[x,y]}
        self.nom = nom
        self.team = team
        self._soldats = soldats
        self._batiments=batiments
        self._ressources=ressources
        self._batiments = {}
        self._soldats = {'archer':[], 'arbaletrier':[], 'berserker':[],'chevalier':[],'cavalier':[], 'batisseur':[]}
        print(self.get_soldats)

        #player(ClasseJ.appel_classe,20,30,self.team)
        Game.canva.bind_all('<space>',self.autent)
        Joueur.joueurs.append(self)
        self.add_soldats()
        print(self.get_soldats)

    def add_soldats(self):
        if self.get_soldats()['batisseur']==[]:    
            player(ClasseJ.appel_classe[-1],20,40,self.team)
        return None
    def add_batiments(self,choix,x,y,t):
        return None
    def autent(self):
        return None
    def get_soldats(self):
        return self._soldats
    
    def set_soldats(self,classe,id,x,y):
        '''
        print(self._soldats)
        print(self._soldats[f'{classe}'])
        print(id,x,y)
        '''
        self._soldats[f'{classe.nom}']=self._soldats[f'{classe.id}'].append([id,x,y])

    property(set_soldats,get_soldats)
        

    
    
        
class Batiment:

    def __init__(self,nom,pv,force):
        self.nom=nom
        self.pv = pv
        self.force = force
                
    def caserne(self,choix,nb_soldats):
        #permet de creer une unité 
        self.Joueur.add_soldats(choix,nb_soldats)

    def ferme(self):
        #ajoute des ressources aux joueurs
        return None


        



        

class ClasseJ:
    appel_classe = []
    def __init__(self,id,basepv,arme,baseforce):
        self._basepv=basepv
        self.arme = arme
        self.id=id
        self.baseforce = baseforce
        ClasseJ.appel_classe.append(self)
        print(ClasseJ.appel_classe.index(self.id))

    def getpv(self):
        return self.basepv

    basepv = property(getpv)

    




class Arme:
    appel_arme = 0
    def __init__(self,id,degats,portee):
        self.id = id
        self._degats = degats
        self.portee = portee
        Arme.appel_arme = self


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
    




class Game:
  
    fenetre = tk.Tk()
    canva = tk.Canvas(fenetre, width=1000, height=1000)
    img=0
    color_tablo=["red", "blue","green","yellow","purple","pink"]
    tour = 0
    user_controler = 0
    entrain_bouger = {}
    classe_game = 0
    i = 0
    p = False
    score_player_1=Label(fenetre)
    canva_over = 0

    def __init__(self, largeur, hauteur, maap, p):
        self.largeur = largeur
        self.hauteur = hauteur
        self.maap = maap
        self.p = p
        Game.classe_game = self 

    def caillou_verif(self,azaz):
        print("hehe")
        
        trajex = Game.canva.create_line(Map.joueur[Map.prenom[Game.user_controler-1]][0]+5,Map.joueur[Map.prenom[Game.user_controler-1]][1]+5  ,azaz[0]+5  ,azaz[1]+5 ,fill="red" )
        #creer un segment entre les deux joueurs
        traj = list(Game.canva.find_overlapping(Game.canva.coords(trajex)[0],Game.canva.coords(trajex)[1] ,Game.canva.coords(trajex)[2] ,Game.canva.coords(trajex)[3]))
        #selectionne tous les items dans la zone 
        #entre les deux joueurs
        traj = list(filter(lambda x: (x>len(self.p)) and (x<len(self.p)+len(Map.obstacle_dic)),traj))#1 et deux sont les deux joueurs , de 3 23 ce sont lesz obstacles , et de 24 a 124 ce sont les lignes du tableau 
        print(list(Game.canva.find_overlapping(0,0,500,500)))
        for i in range(len(traj)):#fait pour tous les obstacles dans le périmetre
            obstacl_traj = list(Game.canva.find_overlapping(Map.obstacle_dic[traj[i]-(len(self.p)-1)][0],Map.obstacle_dic[traj[i]-(len(self.p)-1)][1],(Map.obstacle_dic[traj[i]-(len(self.p)-1)][0])+10,Map.obstacle_dic[traj[i]-(len(self.p)-1)][1]+10))

            #items.canva   1-2=joueurs , 3-23 obstacles , 24-124 lignes du plateau , 125 trajex
            print(obstacl_traj)
            if obstacl_traj[-1] > len(self.p)+len(Map.obstacle_dic):
                #si l item a pour id +124 il est un TRAJEX
                #Pour tous x ayant un id > 124 dans le canva ,id sera supprimé car un TRAJEX
                Game.canva.delete(list(filter(lambda x: x>len(self.p)+len(Map.obstacle_dic),list(Game.canva.find_all()))))
                return True
        Game.canva.delete(list(filter(lambda x: x>len(self.p)+len(Map.obstacle_dic),list(Game.canva.find_all()))))
        #Pour tout x ayant un id > 124 dans le canva ,id sera supprimé car un TRAJEX
        return False

    def coordsSouris(self,event):
        print(event.x, event.y)
        curseur = list(filter(lambda x:x <= len(self.p),Game.canva.find_overlapping(event.x-5,event.y-5,event.x+5 ,event.y+5)))
        if curseur != []: 

            if Game.user_controler != curseur[0]:
                Game.user_controler = curseur[0]
                print(f'vous controlez le joueur {Game.user_controler}')
        else:
            Game.user_controler = 0
    
    def bouger_real(self,event):
        '''
        bouton droit de la souris 
        si rien a été selectioné avec le clic gauche auparavant Game.user_controler = 0
        si il est deja entrain de bouger arrete la boucle bouger est met son attitude a False 
        si son attitude == True ca veut dire que le joueur est entrain de bouger
        si le joueur était immobile le dico Game.entrain_bouger du joueur passe en True, change les coordonnées que l on veut suivre
        et appele go_to qui calcule la pente pour ensuite appeller bouger qui vat faire toutes les verif et faire une boucle Game.after.... 
        '''
        curseur = list(filter(lambda x:x <= len(self.p),Game.canva.find_overlapping(event.x-5,event.y-5,event.x+5 ,event.y+5)))
        if curseur != []:
            print(self.caillou_verif(Map.joueur[Map.prenom[curseur[0]-1]]))
        if Game.user_controler ==0:
            return None
        
        if Game.entrain_bouger[Game.user_controler][0] == True :
            Game.fenetre.after_cancel(self.bouger)
            Game.fenetre.after_cancel(self.bouger)
            Game.fenetre.after_cancel(self.bouger)
            Game.entrain_bouger[Game.user_controler][0] = False 
            return None
        else:
            print(Game.user_controler,event.x,event.y)
            Game.entrain_bouger[Game.user_controler][0] = True
            Game.entrain_bouger[Game.user_controler][1] = event.x 
            Game.entrain_bouger[Game.user_controler][2] = event.y
            self.go_to(event.x,event.y)
        


    def collision_border(self,user):
        '''
        basiq too
        '''
        if (Map.joueur[Map.prenom[user]][0] > 500) or (Map.joueur[Map.prenom[user]][1] > 500) or (Map.joueur[Map.prenom[user]][0]< 0) or (Map.joueur[Map.prenom[user]][1]< 0):
            return True
        return False

    def collision_obstacle(self,user):
        '''
        ca c est basiq
        '''

        caillou_collision_player = list(Game.canva.find_overlapping(Map.joueur[Map.prenom[user]][0],Map.joueur[Map.prenom[user]][1] ,Map.joueur[Map.prenom[user]][0]+10 ,Map.joueur[Map.prenom[user]][1]+10))
        caillou_collision_player = list(filter(lambda x: (x>len(self.p)) and (x<21+len(self.p)),caillou_collision_player))
        if caillou_collision_player != []:
            return True
        return False
    
    def deplacement_finish(self,user,x,y):
        '''
        marche pas , faut que les coordonnées du joueur soient les memes que celles de la position choisi qui est dans le dico Game.entrain_bouger
        x,y coordonnées actuelles des joueurs 
        '''
        if (round(x) == round(Game.entrain_bouger[user+1][1])) and (round(y) == round(Game.entrain_bouger[user+1][2])):
            print("tu es arrivé")
            return True
        return False

    def go_to(self,xe,ye):
        '''
        la pente pour la direction du carré
        '''
        x = (xe - Map.joueur[Map.prenom[Game.user_controler-1]][0])/100
        y = (ye - Map.joueur[Map.prenom[Game.user_controler-1]][1])/100
        print(x,y)
        self.bouger(Game.user_controler-1,x,y)
        Game.fenetre.after_cancel(self.bouger) 
         

    def bouger(self,user,x,y):
        '''
        si l attitude a changé entre temps , la condition de bouge_real aura arreté la boucle mais il faut tout de meme return None pour vraiemnt la boucler
        '''
        if Game.entrain_bouger[user+1][0] == False:
   
            return None
        Game.canva.pack()
        #collision border
        Map.joueur[Map.prenom[user]]=Map.joueur[Map.prenom[user]][0] + x ,Map.joueur[Map.prenom[user]][1] + y
        

        if self.deplacement_finish(user,Map.joueur[Map.prenom[user]][0],Map.joueur[Map.prenom[user]][1]) == True :
            Game.fenetre.after_cancel(self.bouger)
            Game.entrain_bouger[user+1][0] = False
            return None   

        if self.collision_border(user) == True:
            Map.joueur[Map.prenom[0]]=Map.joueur[Map.prenom[user]][0] - x ,Map.joueur[Map.prenom[user]][1] - y
            Game.fenetre.after_cancel(self.bouger)
            Game.entrain_bouger[user+1][0] = False
            return None   

        if self.collision_obstacle(user) == True:
            Map.joueur[Map.prenom[0]]=Map.joueur[Map.prenom[user]][0] - x ,Map.joueur[Map.prenom[user]][1] - y
            Game.fenetre.after_cancel(self.bouger) 
            Game.entrain_bouger[user+1][0] = False 
            return None
        
        Game.canva.move(Map.trouv[user],x,y) 
        Game.fenetre.after(50,self.bouger,user,x,y) 

    def creation(self, largeur, hauteur):
        
        #Game.fenetre.geometry('%sx%s'%(self.largeur+50,self.hauteur+50))
        Game.fenetre.geometry('%sx%s'%(550,750))
        Game.canva.pack()
        
        for i in range(len(self.p)):
            Game.entrain_bouger[i+1] = [False,0,0]


        for i in range(len(Map.obstacle_dic)):
            Game.canva.create_rectangle(Map.obstacle_dic[i][0],Map.obstacle_dic[i][1],Map.obstacle_dic[i][0]+10,Map.obstacle_dic[i][1]+10,fill="black")
 

        Game.fenetre.configure(bg='black')
        Game.score_player_1.configure(bg='green') 
        Game.score_player_1.pack()
        Bouton_Quitter=Button(Game.fenetre, text ='Quitter', command = Game.fenetre.destroy)#boutton pour quitter le jeu
        Bouton_Quitter.pack()

        Game.canva.bind("<Button-1>", self.coordsSouris)
        Game.canva.bind("<Button-3>", self.bouger_real)

        Game.canva.bind_all('<space>',)
        Game.canva.create_rectangle( 10,510 ,510 ,700 ,fill="red" )
        Game.canva.create_rectangle( 20,520 ,70 ,570 ,fill="green" )
        Game.canva.create_rectangle( 350,520 ,500 ,690 ,fill="green" )
        self.mise_a_jour()
        Game.canva_over = len(Game.canva.find_overlapping(0,0,550,750))
        print(Game.canva_over)
        Game.fenetre.mainloop()#affiche le canv

    def placement_nv_pions(self,id,team,x,y):
        return None   
    def mise_a_jour(self):
        file_path = "C:/Users/ralit/OneDrive/Bureau/Reproject/Reproject/image/cavalier.png"
        Game.img = ImageTk.PhotoImage(Image.open(file_path))  
        Game.canva.create_image(45, 545, image=Game.img)
        
    
class Map:
    trouv = []
    joueur = {}
    prenom = []
    obstacle_dic= {}
    

    def __init__(self,x,y,ob):
        self.x = x
        self.y = y
        self.ob = ob
        self.créer_obstacl(self.ob)

    def créer_obstacl(self,obstacle):
        '''
        obstacle:int
        '''
        for i in range(obstacle):
            Map.obstacle_dic[i] = random.randint(0,round(self.x/10))  *10 , random.randint(0, round(self.y/10)) *10

from jeuV2xx import *
from def_armes_classexx import *