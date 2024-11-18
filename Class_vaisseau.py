#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation des classes objet du vaisseau et des aliens présent dans le jeu Space Invader avec leur atributs de mouvement et de tir
#Fait le 18 novembre 2024
# A améliorer: Calibrer vitesse des aliens et vaisseau ainsi que le tir des balles du vaisseau et du nombre de tir par seconde
# A ajouter: Ajouter les dégats pouvant être pris par les vaisseaux et aliens (vie)

import random as rd

class Vaisseau:  # implémentation de la classe vaisseau utilisée par le joueur lorsqu'il démarre une parte 

    def __init__(self,canvas):
        self.canvas=canvas
        self.x = 350
        self.y = 600
        self.v = 1
        self.dt = 8
        self.dx = 1
        self.dy = 0
        self.create()           #Ajout des fonctions nécessaire au fonctionnement du vaisseau
        self.toucher_bordure()
        self.key_handler()

    def create(self):       #Création du vaisseau sur la page de jeu
        self.rectangle=self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50,fill='blue')

    def toucher_bordure(self):      
        canvas_width = self.canvas.winfo_width()  # Largeur du canevas
        canvas_height = self.canvas.winfo_height()  # Hauteur du canevas

        # Vérifie si le personnage touche les bords gauche ou droit
        if self.x <= 0 or self.x + 50 >= canvas_width:
            self.dx = -self.dx  # Inverse la direction horizontale

            self.y += 25
            self.canvas.move(self.rectangle,0,10)

        # Vérifie si le personnage touche les bords haut ou bas
        if self.y <= 0 or self.y + 50 >= canvas_height:
            self.dy = -self.dy

    def key_handler(self):              #Fonctions qui permet de renvoyer aux fonctions lors de l'appuie sur différentes touches du clavier
        self.canvas.bind("<Right>", self.Right)
        self.canvas.bind("<Left>", self.Left)
        self.canvas.bind("<space>",self.tir)
        self.canvas.focus_set()    
        
    def Left(self,event):       #Fonctions qui fait bouger à gauche le vaisseau quand on appuie sur la flèche de gauche
        x=-50
        y=0
        self.canvas.move(self.rectangle,x,y)
    
    def Right(self,event):      #Fonctions qui fait bouger à droite le vaisseau quand on appuie sur la flèche de droite
        x=50
        y=0
        self.canvas.move(self.rectangle,x,y)
    
    def tir(self,event):        #Fonctions qui ance un projectile lorsque l'on appuie sur la barre d'espace
        coord=self.canvas.coords(self.rectangle)
        self.x=coord[0]
        Projectile(self.x + 25, self.y,-8, self.canvas)



class Alien:        #Implémente la classe alien avec ses différentes caractéristiques
    def __init__(self,canvas):
        self.canvas=canvas
        self.x=350                      #Définie la position de l'alien
        self.y=30
        self.v=1
        self.dt=8
        self.dt2=rd.randint(400,2000)
        print(self.dt2)
        self.dx=1
        self.dy=0
        self.create()
        self.bouger()
        self.toucher_bordure()
        self.tir()

    def create(self):       #Fonctions qui crée les aliens
        self.rectangle=self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50,fill='red')

    def bouger(self):       #Fonctions qui fait bouger l'alien horizontalement
        self.canvas.move(self.rectangle, self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy
        self.toucher_bordure()  # Vérifie si le personnage touche un bord
        self.canvas.after(self.dt, self.bouger)

    def toucher_bordure(self):
        canvas_width = self.canvas.winfo_width()  # Largeur du canevas
        canvas_height = self.canvas.winfo_height()  # Hauteur du canevas

        # Vérifie si le personnage touche les bords gauche ou droit
        if self.x <= 0 or self.x + 50 >= canvas_width:
            self.dx = -self.dx  # Inverse la direction horizontale

            self.y += 25
            self.canvas.move(self.rectangle,0,10)

        # Vérifie si le personnage touche les bords haut ou bas
        if self.y <= 0 or self.y + 50 >= canvas_height:
            self.dy = -self.dy

    def tir(self):      #Fonctions qui fait tirer l'alien automatiquement avec un intervallee de tir pris au hasard
        self.dt2=rd.randint(400,2000)
        coord=self.canvas.coords(self.rectangle)
        self.x=coord[0]
        Projectile(self.x + 25, self.y - 25,8, self.canvas)
        self.canvas.after(self.dt2,self.tir)