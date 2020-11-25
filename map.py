from __future__ import annotations
import random
from _class_ import *

import tkinter as tk
from tkinter import *
#TENGO UNA PROBLEMA MUY IMPORTANTES QUE quand on bouge trop le jeu plante no sabo porque


class Map:
    trouv = []
    mapa = {}
    prenom = []
    fenetre = tk.Tk()
    canva = tk.Canvas(fenetre, width=500+10, height=500+10)#PROBLEMOS il faut que ca soit une VARIABLE

    def __init__(self,x,y,ob):
        self.x = x
        self.y = y
        self.ob = ob
        self.création(self.x,self.y)
    
    def droite(self,event):
        self.bouger(10,0)

    def gauche(self,event):
        self.bouger(-10,0)

    def haut(self,event):
        self.bouger(0,-10)

    def bas(self,event):
        self.bouger(0,10)


    def création(self,x,y):
  
        self.obstacl(self.ob)#lance la fonction obstacle 
        Map.fenetre.geometry('%sx%s'%(self.x+50,self.y+50))
        
        Map.canva.pack()
        for key in Map.mapa:#si dans mapa il y a un str alor le faire en bleue car c est un joueur
            if type(key) == str : 
                Map.trouv.append(Map.canva.create_rectangle(Map.mapa[key][0],Map.mapa[key][1],Map.mapa[key][0]+10,Map.mapa[key][1]+10,fill="blue"))
            else:
                Map.canva.create_rectangle(Map.mapa[key][0],Map.mapa[key][1],Map.mapa[key][0]+10,Map.mapa[key][1]+10,fill="grey")
        
        for i in range(round(self.x/10)):
            Map.canva.create_line(i*10 ,0  ,i*10  ,self.x , fill="black")#lignes

        for i in range(round(self.x/10)):
            Map.canva.create_line(0 , i*10 , self.x , i*10 , fill="black")#lignes

        Bouton_Quitter=Button(Map.fenetre, text ='Quitter', command = Map.fenetre.destroy)#boutton pour quitter le jeu
        Bouton_Quitter.pack()
        Map.canva.bind_all('<Right>', self.droite)#fleches directionnelles pour les events
        Map.canva.bind_all('<Left>', self.gauche)
        Map.canva.bind_all('<Up>', self.haut)
        Map.canva.bind_all('<Down>', self.bas)
        Map.fenetre.mainloop()#affiche le canva
        

    def créer_obstacl(self,obstacle):
        for i in range(obstacle):
            Map.mapa[i] = random.randint(0,round(self.x/10))  *10 , random.randint(0, round(self.y/10)) *10 #création des obstacle , physique 
            #avec player pas encore faite 

    def bouger(self,dx,dy):
        player.tour_par_tour()      
        Map.canva.pack()
        Map.canva.move(Map.trouv,dx,dy)