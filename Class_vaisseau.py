#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation des classes objet du vaisseau et des aliens présent dans le jeu Space Invader avec leur atributs de mouvement et de tir
#Fait le 18 novembre 2024
# A améliorer: Calibrer vitesse des aliens et vaisseau ainsi que le tir des balles du vaisseau et du nombre de tir par seconde
# A ajouter: Ajouter les dégats pouvant être pris par les vaisseaux et aliens (vie)

import random as rd
from Class_Projectile import Projectile

class Vaisseau:
    # implémentation de la classe vaisseau utilisée par le joueur lorsqu'il démarre une parte 
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 350
        self.y = 600
        self.vie = 3
        self.Liste_Projectile = []
        self.rectangle = self.create()
        self.key_handler()

    def create(self):
        return self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill='blue')

    def key_handler(self):
        self.canvas.bind("<Right>", self.Right)
        self.canvas.bind("<Left>", self.Left)
        self.canvas.bind("<space>", self.tir)
        self.canvas.focus_set()

    def Left(self, event):
        if self.canvas.coords(self.rectangle)[0] > 0:
            self.canvas.move(self.rectangle, -20, 0)

    def Right(self, event):
        if self.canvas.coords(self.rectangle)[2] < self.canvas.winfo_width():
            self.canvas.move(self.rectangle, 20, 0)

    def tir(self, event):
        coord = self.canvas.coords(self.rectangle)
        x = (coord[0] + coord[2]) / 2
        y = coord[1]
        self.Liste_Projectile.append(Projectile(x, y, -1, 10, 1, self.canvas))



class Alien:
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
        return self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill='red')

    def bouger(self):
        self.canvas.move(self.rectangle, self.dx, 0)
        self.x += self.dx
        if self.toucher_bordure():
            self.dx = -self.dx
            self.canvas.move(self.rectangle, 0, 25)
        self.canvas.after(50, self.bouger)

    def toucher_bordure(self):
        canvas_width = self.canvas.winfo_width()
        coords = self.canvas.coords(self.rectangle)
        return coords[0] <= 0 or coords[2] >= canvas_width

    def tir(self):
        coord = self.canvas.coords(self.rectangle)
        x = (coord[0] + coord[2]) / 2
        y = coord[3]
        self.projectiles.append(Projectile(x, y, 1, 5, 1, self.canvas))
        self.canvas.after(rd.randint(2000, 4000), self.tir)