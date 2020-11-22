from __future__ import annotations
import random
from _class_ import *
import tkinter as tk

class Map:
    mapa = {}
    lenghtmapa = []
    fenetre = tk.Tk()

    def __init__(self,x,y,ob):
        self.x = x
        self.y = y
        self.ob = ob
        self.création(self.x,self.y)
        
    def création(self,x,y):
        self.obstacl(self.ob)
        Map.lenghtmapa= [self.x,self.y]
        Map.fenetre.geometry('%sx%s'%(self.x+50,self.y+50))
        canva = tk.Canvas(Map.fenetre, width=self.x+10, height=self.y+10)
        canva.pack()
        for key in Map.mapa:
            if type(key) == str : 
                canva.create_rectangle(Map.mapa[key][0],Map.mapa[key][1],Map.mapa[key][0]+10,Map.mapa[key][1]+10,fill="blue")
                print(key)
            else:
                canva.create_rectangle(Map.mapa[key][0],Map.mapa[key][1],Map.mapa[key][0]+10,Map.mapa[key][1]+10,fill="grey") 
        Map.fenetre.mainloop()
    
    def obstacl(self,obstacle):
        for i in range(obstacle):
            Map.mapa[i] = random.randint(0, self.x) , random.randint(0, self.y)