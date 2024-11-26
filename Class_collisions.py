#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation de la classe Jeu du space invader
# #Fait le 18 novembre 2024
# A améliorer: l'algorithme d'apparition des aliens
# A ajouter: Gérer les interactions entre les projectils, les blocs et les personnages


import tkinter as tk

class Collisions:
    def __init__(self,canvas,Vaisseau):
      self.canvas=canvas
      self.Vaisseau=Vaisseau
      self.col()


    def col(self):
        indice_a_supprimer=[]
        for i in range(len(self.Vaisseau.Liste_Projectile)):
             
             projectile=self.Vaisseau.Liste_Projectile[i]

             for personnage in self.Jeu.Listes_Personnages:

                if personnage!=0 and projectile.x < personnage.x + 10 and projectile.x < personnage.x-10 and projectile.y < personnage.y+10 and projectile.y < personnage.y-10:
                    personnage.vie += -projectile.degat
                    projectile.canvas.delete(projectile.circle)
                    indice_a_supprimer.append(i)

                    if personnage.vie == 0 :

                        personnage=0
                        personnage.canvas.delete(personnage.rectangle)
        n=0
        for j in range(len(indice_a_supprimer)):
            self.Jeu.Liste_Projectile.pop(indice_a_supprimer[j]-n)
        