#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation des classes objet du vaisseau et des aliens présent dans le jeu Space Invader avec leur atributs de mouvement et de tir
#Fait le 18 novembre 2024
# A améliorer: Calibrer vitesse des aliens et vaisseau ainsi que le tir des balles du vaisseau et du nombre de tir par seconde
# A ajouter: Ajouter l'image du vaisseau

import random as rd
from Class_Projectile import Projectile

class Vaisseau:
    # implémentation de la classe vaisseau utilisée par le joueur lorsqu'il démarre une partie
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 350
        self.y = 600
        self.vie = 3
        self.Liste_Projectile = []
        self.rectangle = self.create()
        self.key_handler()

    def create(self):
        #fonction qui crée le vaisseau
        return self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50, fill='blue')

    def key_handler(self):
        #fonction qui permet de gérer l'interaction entre le clavier du joueur et les mouvements
        
        self.canvas.bind("<Right>", self.Right)
        self.canvas.bind("<Left>", self.Left)
        self.canvas.bind("<space>", self.tir)
        self.canvas.focus_set()

    def Left(self, event):
        #fonction qui fait bouger le personnage à gauche quand l'utilisateur appuye sur flèche de gauche
        
        if self.canvas.coords(self.rectangle)[0] > 0:
            self.canvas.move(self.rectangle, -20, 0)


    def Right(self, event):
        #fonction qui fait bouger le personnage à droite quand l'utilisateur appuye sur flèche de droite
        
        if self.canvas.coords(self.rectangle)[2] < self.canvas.winfo_width():
            self.canvas.move(self.rectangle, 20, 0)


    def tir(self, event):
        #fonction qui fait tirer le personnage quand l'utilisateur appuye sur barre espace
        
        coord = self.canvas.coords(self.rectangle)
        x = (coord[0] + coord[2]) / 2
        y = coord[1]
        self.Liste_Projectile.append(Projectile(x, y, -1, 10, 1, self.canvas))

