#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation de la classe Jeu du space invader
# #Fait le 18 novembre 2024
# A améliorer: l'algorithme d'apparition des aliens
# A ajouter: Gérer les interactions entre les projectils, les blocs et les personnages


import tkinter as tk
from Class_Jeu import Jeu




class Collisions:
    def __init__(self,canvas,Jeu):
      self.canvas=canvas
      self.Jeu=Jeu
      self.col()


    def col(self):
        for projectile in Jeu.Liste_Projectiles:
             for personnage in Jeu.Listes_Personnages:
                if personnage == 0:
               
                elif projectile.x < personnage[0].x + 10  and   projectile.x < personnage[0].x - 10   and   projectile.y < personnage[0].y + 10   and   projectile.y < personnage[0].y - 10:
                    personnage[1] += -projectile.degat
                    destroy(projectile)
                    if personnage[1] == 0 :
                        destroy(personnage[1])
                        personnage=0

