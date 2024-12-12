#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation de la classe projectils
# #Fait le 18 novembre 2024
# A améliorer: ajouter les vies supplémentaires qui tomberont à la mort d'un boss
# # A ajouter: le skin du projectile


import tkinter as tk


class Projectile:           #classe gérant l'ensemble des projectiles qui soit du vaisseau ou des aliens
    def __init__(self, x, y, direction, vitesse, degat, canvas):
        self.x = x
        self.y = y
        self.dy = direction * vitesse
        self.canvas = canvas
        self.degat = degat
        self.circle = self.create()
        self.bouger()

    def create(self):           #fonction qui crée le projectile en forme d'oval
        return self.canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill='white')

    def bouger(self):           #fonction qui gère les mouvements du projectile
        self.y += self.dy
        self.canvas.move(self.circle, 0, self.dy)
        if self.toucher_bordure():
            self.canvas.delete(self.circle)
        else:
            self.canvas.after(30, self.bouger)

    def toucher_bordure(self):          #fonction qui gère l'interaction entre les bordures et les projectiles
        canvas_height = self.canvas.winfo_height()
        return self.y <= 0 or self.y >= canvas_height
