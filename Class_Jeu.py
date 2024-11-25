#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation de la classe Jeu du space invader
# #Fait le 18 novembre 2024
# A améliorer: l'algorithme d'apparition des aliens
# A ajouter: Gérer les interactions entre les projectils, les blocs et les personnages


import tkinter as tk
import Class_Projectile
import Main_Space_Invader
import class_bloc
from random import randint

class Jeu():

    def __init__(fenetre):
        self.Liste_Personnages = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.indice_niveaux = [0,1,1,1,1,1,1,2,2,2,2,3]
        self.Liste_Projectile = []

    def create_Alien():
        # cette fontcion est un algoritme qui permet l'apparition d'aliens
        #les aliens apparaissent que si un element de la liste ListePersonnage est vide pour limiter le nombre d'aliens
        L=[]
        for i in range(1,len(self.Liste_Personnage)):
            if self.Liste_Personnage[i]==0:
                L.append(i)
        indiceL=randint(len(L))
        indice=L[indiceL]
        self.Liste_Personnages[indice] = Alien(self.indice_niveaux[indice])




    Visuel()
    Joueur= Vaisseau()
    Bloc1= bloc()
    Bloc2= bloc()
    self.Liste_Personnage[0],self.Liste_Personnage[10],self.Liste_Personnage[11]=[Joueur,3],[Bloc1,3],[Bloc2,3]
    



    canvas.after(10,create_Alien())