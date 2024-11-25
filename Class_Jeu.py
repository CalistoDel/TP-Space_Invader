#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation de la classe Jeu du space invader
# #Fait le 18 novembre 2024
# A améliorer: l'algorithme d'apparition des aliens
# A ajouter: Gérer les interactions entre les projectils, les blocs et les personnages


import tkinter as tk
from Class_Projectile import Projectile
from Main_Space_Invader import Visuel
from class_bloc import bloc
from Class_vaisseau import Vaisseau , Alien
from Class_collisions import Collisions
from random import randint


class Jeu:

    def __init__(self,fenetre):
        self.Liste_Personnages = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.indice_niveaux = [0,1,1,1,1,1,1,2,2,2,2,3]
        self.Liste_Projectile = []
        self.score = 0
        self.fenetre = fenetre
        self.create_Alien()
        self.label()
        self.score()
        self.start()

    def create_Alien(self):
        # cette fontcion est un algoritme qui permet l'apparition d'aliens
        #les aliens apparaissent que si un element de la liste ListePersonnage est vide pour limiter le nombre d'aliens
        L=[]
        for i in range(1,len(self.Liste_Personnages)):
            if self.Liste_Personnages[i] ==0 :
                L.append(i)

        indiceL=randint(len(L))
        indice=L[indiceL]
        self.Liste_Personnages[indice] = Alien(self.indice_niveaux[indice])

    


    def score(self,alien):
        point=alien.niveau
        if alien.niveau == 3 :
            point = 4
        score += point
    


    def label(self):        #fonction qui créer tous les textes présent sur la fenêtre 
        self.affichage_score = tk.Label( self,text = 'Score : '+ str(self.score) )
        self.affichage_score.pack( side = 'top' )

    




    def start(self):
        Visuel()
        Joueur= Vaisseau()
        Bloc1= bloc(50,self.fenetre)
        Bloc2= bloc(100,self.fenetre)
        self.Liste_Personnage[0],self.Liste_Personnage[10],self.Liste_Personnage[11]=Joueur,Bloc1,Bloc2




    canvas.after(10,create_Alien())
