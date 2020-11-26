import random
from _class_ import *

import tkinter as tk
from tkinter import *
class Map:
    trouv = []
    mapa = {}
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
