import random
from _class_ import *

import tkinter as tk
from tkinter import *
#TENGO UNA PROBLEMA MUY IMPORTANTES QUE quand on bouge trop le jeu plante no sabo porque


class Map:
    trouv = []
    mapa = {}
    prenom = []
    obstacle_dic= {}
#PROBLEMOS il faut que ca soit une VARIABLE

    def __init__(self,x,y,ob):
        self.x = x
        self.y = y
        self.ob = ob
        self.créer_obstacl(self.ob)

    def créer_obstacl(self,obstacle):
        for i in range(obstacle):
            Map.obstacle_dic[i] = random.randint(0,round(self.x/10))  *10 , random.randint(0, round(self.y/10)) *10 #création des obstacle , physique 
            #avec player pas encore faite

