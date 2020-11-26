from map import * 

class player:
    tablo_player = []
    def __init__(self,nom,classe,x,y): #initialiseur
        self.classe = ClasseJ
        self._pv = classe._basepv #attribut public
        self.x = x
        self.y = y
        self.nom = nom 
        Map.mapa[self.nom] = self.x*10,self.y*10#rentre les coordonnées du joueurs dans mapa
        Map.prenom.append(self.nom)
        player.tablo_player.append(self)
        Game.canva.bind_all('<space>',self.attak )




    def get_pv(self): #permet de recuperer les pv pour l'affichage
        return self._pv

    def set_pv(self, val): #permet de set les pv quand on va se faire taper
        self._pv += val

    def attak(self,event): #change place dans tableau--> PB
        if Game.tour == 0:
            player.tablo_player.append(player.tablo_player[0])
            player.tablo_player.pop(0)
        player.tablo_player[0].attaquer(player.tablo_player[1])
        

    def attaquer(self,adv):
        
        player1 = []
        player2 = []
        
        
        touché_caillou = False
        #ente
        for i in range(len(Map.obstacle_dic)):#
            if (Map.mapa[Map.prenom[0]][0]-Map.obstacle_dic[i][0]) == 0 :
                gf = round( Map.obstacle_dic[i][1] - Map.mapa[Map.prenom[0]][1])*100   
                player1.append(gf)
            else: 
                gf = round((( Map.obstacle_dic[i][1] - Map.mapa[Map.prenom[0]][1])  / (Map.obstacle_dic[i][0] - Map.mapa[Map.prenom[0]][0]))*100)   
                player1.append(gf)
            if (Map.obstacle_dic[i][0] - Map.mapa[Map.prenom[1]][0]) == 0 :
                gf1 = round( Map.obstacle_dic[i][1] - Map.mapa[Map.prenom[1]][1])*100   
                player2.append(gf1)
            else: 
                gf1 = round((( Map.obstacle_dic[i][1] - Map.mapa[Map.prenom[1]][1])  / (Map.obstacle_dic[i][0] - Map.mapa[Map.prenom[1]][0]))*100)   
                player2.append(gf1)

            if player1[i] == player2[i]:

                if ((Map.obstacle_dic[i][0]>Map.mapa[Map.prenom[0]][0])and(Map.obstacle_dic[i][0]>Map.mapa[Map.prenom[1]][0]))or ((Map.obstacle_dic[i][1]>Map.mapa[Map.prenom[0]][1])and(Map.obstacle_dic[i][1]>Map.mapa[Map.prenom[1]][1])):
                    print('L ennemi est a découvert Chef')
                else:
                    touché_caillou = True
                    print('dommage tu as touché un caillou')  
#pente
        adv.set_pv(-80)
        advpv = adv.get_pv()
        selfpv = self.get_pv()
        if (advpv < 0) or (selfpv<0):
            print(f'{player.tablo_player[0].nom} a gagné')
            Game.fenetre.destroy()
        print(f'joueur : {self.nom}, pv : {self.pv}')
        print(f'joueur : {adv.nom}, pv : {adv.pv}')
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
    fenetre = tk.Tk()
    canva = tk.Canvas(fenetre, width=500+10, height=500+10)

    def __init__(self, largeur, hauteur, maap, p1, p2):
        self.largeur = largeur
        self.hauteur = hauteur
        self.maap = maap
        self.p1 = p1
        self.p2 = p2
        self._tour = 1

    def get_tour(self):
        return self._tour

    def set_tour(self, val):
        self._tour += val

    tour = property(get_tour, set_tour)
    
    def droite(self,event):
        self.bouger(10,0)

    def gauche(self,event):
        self.bouger(-10,0)

    def haut(self,event):
        self.bouger(0,-10)

    def bas(self,event):
        self.bouger(0,10)

    def bouger(self,dx,dy):
        if self._tour > 6:
            Map.trouv.append(Map.trouv[0])
            Map.trouv.pop(0)
            Map.prenom.append(Map.prenom[0])
            Map.prenom.pop(0)
            self._tour = 0
        else : self.set_tour(1)
        Game.canva.pack()
        #collision border
        Map.mapa[Map.prenom[0]]=Map.mapa[Map.prenom[0]][0] + dx ,Map.mapa[Map.prenom[0]][1] + dy
        if (Map.mapa[Map.prenom[0]][0] > 500) or (Map.mapa[Map.prenom[0]][1] > 500) or (Map.mapa[Map.prenom[0]][0]< 0) or (Map.mapa[Map.prenom[0]][1]< 0):
            Map.mapa[Map.prenom[0]]=Map.mapa[Map.prenom[0]][0] - dx ,Map.mapa[Map.prenom[0]][1] - dy
        else:
            Game.canva.move(Map.trouv[0],dx,dy)
        

    def creation(self, largeur, hauteur):
        Game.fenetre.geometry('%sx%s'%(self.largeur+50,self.hauteur+50))
        Game.canva.pack()

        for key in Map.mapa:#si dans mapa il y a un str alor le faire en bleue car c est un joueur
            color_tablo=["red", "blue"]
            Map.trouv.append(Game.canva.create_rectangle(Map.mapa[key][0],Map.mapa[key][1],Map.mapa[key][0]+10,Map.mapa[key][1]+10,fill=color_tablo[i]))
            i+=1
        for i in range(len(Map.obstacle_dic)):
            Game.canva.create_rectangle(Map.obstacle_dic[i][0],Map.obstacle_dic[i][1],Map.obstacle_dic[i][0]+10,Map.obstacle_dic[i][1]+10,fill="grey")
        
        for i in range(round(self.largeur/10)+1):
            Game.canva.create_line(i*10 ,0  ,i*10  ,self.largeur+10 , fill="black")#colonnes

        for i in range(round(self.largeur/10)+1):
            Game.canva.create_line(0 , i*10 , self.largeur +10, i*10 , fill="black")#lignes

        

        Bouton_Quitter=Button(Game.fenetre, text ='Quitter', command = Game.fenetre.destroy)#boutton pour quitter le jeu
        Bouton_Quitter.pack()
        Game.canva.bind_all('<Right>', self.droite)#fleches directionnelles pour les events
        Game.canva.bind_all('<Left>', self.gauche)
        Game.canva.bind_all('<Up>', self.haut)
        Game.canva.bind_all('<Down>', self.bas)
        Game.canva.bind_all('<Space>', )
        Game.fenetre.mainloop()#affiche le canva
