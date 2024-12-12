#Fait par Calisto Del Aguila et Bilel Ghouaiel
#Implémentation des caractéristiques visuel de Space Invader, implémentation de la fenêtre et des boutons
# #Fait le 18 novembre 2024
# A améliorer: actualiser le score, proposer une fonction 'rejouer' et mettre un écran de game over quand on perd (ne pas fermer le canva brusquement)
# # A ajouter: une image de fond

#Importation de la librairie tkinter pour la partie visuelle de Space Invader
import tkinter as tk
from random import randint
from Class_vaisseau import Vaisseau
from Class_Alien import Alien
from Class_collisions import Collisions
from Class_Projectile import Projectile


class Visuel(tk.Tk):
#Cette classse s'occupe de créer toute la partie graphique/visuelle de Space Invader
    def __init__(self):
        tk.Tk.__init__(self)         #Création de la fenêtre de jeu
        self.canvas()
        self.label()
        self.Boutton()
        self.menu()

    def label(self):
        #fonction qui créer tous les textes présent sur la fenêtre 
        
        self.score = tk.Label(self,text='Votre score est: 0')
        self.score.pack(side='top')

    def Boutton(self):
        #fonction qui créer les différents bouttons
        
        self.JeuButton = tk.Button(self,text='Jouer', command=self.page_jeu)
        self.QuitButton = tk.Button(self,text='Quitter',command=self.destroy)
        self.QuitButton.pack(side='bottom')
        self.JeuButton.pack()

    def menu(self):
        #fonction qui créer une barre déroulante
        
        self.menubar = tk.Menu(self)
        self.menu1=tk.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Menu',menu=self.menu1)
        self.menu1.add_command(label="Rejouer")
        self.menu1.add_command(label="A propos")
        self.config(menu=self.menubar)


    def canvas(self):
        #fonction qui crée la toile
        
        self.canvas1 = tk.Canvas(self,width= 800, height=700, bg='black')
        self.canvas1.pack()


    def page_jeu(self):
        #fonction qui permet de démarrer la partie de jeu
        
        self.label()
        self.Boutton()
        self.menu()
        self.personnage = Vaisseau(self.canvas1)
        self.aliens = [Alien(self.canvas1) for _ in range(5)]
        self.collisions = Collisions(self.canvas1, self.personnage, self.aliens)


if __name__ == "__main__":
    fenetre = Visuel()
    fenetre.title("Space Invader")
    fenetre.mainloop()

