#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation des classes objet du vaisseau et des aliens présent dans le jeu Space Invader avec leur atributs de mouvement et de tir
#Fait le 18 novembre 2024
# A améliorer: Calibrer vitesse des aliens, la vitesse des projectiles et la cadence de tir en fonction du niveau de l'alien
# A ajouter: Ajouter l'image des différents aliens

import random as rd
from Class_Projectile import Projectile

class Alien:
    #Classe qui gère les aliens (leur création, leur déplacement et leurs tirs)

    def __init__(self, canvas, niveau=1):
        self.canvas = canvas
        self.x = rd.randint(50, 750)
        self.y = rd.randint(30, 150)
        self.niveau = niveau
        self.vie = 3
        self.dx = 2
        self.dy = 0
        self.rectangle = self.create()
        self.bouger()
        self.projectiles = []
        self.tir()

    def create(self):       
        #fonction qui crée les aliens
        return self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill='red')

    def bouger(self):
        #fonction qui crée l'ensemble des mouvements que font les aliens
        
        self.canvas.move(self.rectangle, self.dx, 0)
        self.x += self.dx

        if self.toucher_bordure():
            self.dx = -self.dx
            self.canvas.move(self.rectangle, 0, 25)
        self.canvas.after(50, self.bouger)

    def toucher_bordure(self):
        #fonction qui gère les interactions entre les bordure et les aliens
        
        canvas_width = self.canvas.winfo_width()
        coords = self.canvas.coords(self.rectangle)
        
        return coords[0] <= 0 or coords[2] >= canvas_width


    def tir(self):
        #fonction qui gère les tirs des aliens
        
        coord = self.canvas.coords(self.rectangle)
        x = (coord[0] + coord[2]) / 2
        y = coord[3]
        self.projectiles.append(Projectile(x, y, 1, 5, 1, self.canvas))
        self.canvas.after(rd.randint(2000, 4000), self.tir)