from __future__ import annotations
import random
from _class_ import *
import tkinter as tk
from tkinter import *



class Map:
    tour = 0
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
        #mettre en blanc les carrés sur lesquels je suis passé , probleme Repetition , a revoir,URGENTTT
        Map.canva.create_rectangle(Map.mapa[Map.prenom[0]][0],Map.mapa[Map.prenom[0]][1],Map.mapa[Map.prenom[0]][0]+10,Map.mapa[Map.prenom[0]][1]+10,fill="white")
        Map.mapa[Map.prenom[0]] = Map.mapa[Map.prenom[0]][0]+10,Map.mapa[Map.prenom[0]][1]
        self.bouger()
    def gauche(self,event):
        Map.canva.create_rectangle(Map.mapa[Map.prenom[0]][0],Map.mapa[Map.prenom[0]][1],Map.mapa[Map.prenom[0]][0]+10,Map.mapa[Map.prenom[0]][1]+10,fill="white")
        Map.mapa[Map.prenom[0]] = Map.mapa[Map.prenom[0]][0]-10,Map.mapa[Map.prenom[0]][1]
        self.bouger()
    def haut(self,event):
        Map.canva.create_rectangle(Map.mapa[Map.prenom[0]][0],Map.mapa[Map.prenom[0]][1],Map.mapa[Map.prenom[0]][0]+10,Map.mapa[Map.prenom[0]][1]+10,fill="white")
        Map.mapa[Map.prenom[0]] = Map.mapa[Map.prenom[0]][0],Map.mapa[Map.prenom[0]][1]-10
        self.bouger()
    def bas(self,event):
        Map.canva.create_rectangle(Map.mapa[Map.prenom[0]][0],Map.mapa[Map.prenom[0]][1],Map.mapa[Map.prenom[0]][0]+10,Map.mapa[Map.prenom[0]][1]+10,fill="white")
        Map.mapa[Map.prenom[0]] = Map.mapa[Map.prenom[0]][0],Map.mapa[Map.prenom[0]][1]+10
        self.bouger()


    def création(self,x,y):
        self.obstacl(self.ob)#lance la fonction obstacle 
        Map.fenetre.geometry('%sx%s'%(self.x+50,self.y+50))
        
        Map.canva.pack()
        for key in Map.mapa:#si dans mapa il y a un str alor le faire en bleue car c est un joueur
            if type(key) == str : 
                key = Map.canva.create_rectangle(Map.mapa[key][0],Map.mapa[key][1],Map.mapa[key][0]+10,Map.mapa[key][1]+10,fill="blue")
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

    def obstacl(self,obstacle):
        for i in range(obstacle):
            Map.mapa[i] = random.randint(0,round(self.x/10))  *10 , random.randint(0, round(self.y/10)) *10 #création des obstacle , physique 
            #avec player pas encore faite 

    def bouger(self):
        Map.canva.pack()
        Map.canva.create_rectangle(Map.mapa['marty'][0],Map.mapa[('marty')][1],Map.mapa['marty'][0]+10,Map.mapa['marty'][1]+10,fill="blue")
        Map.fenetre.mainloop()
        Map.tour += 1 

