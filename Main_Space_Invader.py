#Importation de la librairie tkinter pour la partie visuelle de Space Invader
import tkinter as tk
from Class_Projectile import Projectile
import random as rd

class Visuel(tk.Tk):
#Cette classse s'occupe de créer toute la partie graphique/visuelle de Space Invader
    def __init__(self):
        tk.Tk.__init__(self)         #Création de la fenêtre de jeu
        self.image=tk.PhotoImage(file="Espace.gif")
        self.label()
        self.Boutton()
        self.menu()
        self.canvas()
        self.personnage = Vaisseau(self.canvas1)
        self.aliens = Alien(self.canvas1)
        self.collisions=Collisions(self.canvas1,self.personnage,self.aliens)

    def label(self):        #fonction qui créer tous les textes présent sur la fenêtre 
        self.score=tk.Label(self,text='Votre score est:')
        self.score.pack(side='top')

    def Boutton(self):      #fonction qui créer les différents bouttons
        self.JeuButton=tk.Button(self,text='Jouer')
        self.QuitButton=tk.Button(self,text='Quitter',command=self.destroy)
        self.QuitButton.pack(side='bottom')
        self.JeuButton.pack()

    def menu(self):         #fonction qui créer une barre déroulante
        self.menubar=tk.Menu(self)
        self.menu1=tk.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Menu',menu=self.menu1)
        self.menu1.add_command(label="Rejouer")
        self.menu1.add_command(label="A propos")
        self.config(menu=self.menubar)

    def canvas(self):       #fonction qui crée la toile
        self.canvas1=tk.Canvas(self,width= 800, height=700, bg='blue')
        self.canvas1.pack()
        self.canvas1.create_image(800,700,anchor='center',image=self.image)

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
        malisteprojectile=[]
        for i in range(10):
            malisteprojectile.append(Projectile(self.x + 25, self.y - 25,8, self.canvas))
            self.coordonne_projectile=self.canvas.coords(malisteprojectile[i].x,malisteprojectile[i].y)

class Vaisseau:  # implémentation de la classe vaisseau utilisée par le joueur lorsqu'il démarre une parte 

    def __init__(self,canvas):
        self.canvas=canvas
        self.x = 350
        self.y = 600
        self.v = 1
        self.dt = 8
        self.projectiles_vaisseau=[]
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
    
    def tir(self,event):        #Fonctions qui lance un projectile lorsque l'on appuie sur la barre d'espace
        coord=self.canvas.coords(self.rectangle)
        self.x=coord[0]
        self.y=coord[1]
        projectile=Projectile(self.x + 25, self.y,-8, self.canvas)
        self.projectiles_vaisseau.append([projectile.x,projectile.y])
        print(self.projectiles_vaisseau)
        print(self.x,self.y)
        

class Collisions:
    def __init__(self,canvas,mon_vaisseau,mon_alien):
      self.canvas=canvas
      self.mon_vaisseau=mon_vaisseau
      for projec in mon_vaisseau.projectiles_vaisseau:
        if mon_alien.x >= projec.x:
            if mon_alien.y == projec.y:
                self.canvas.delete(mon_alien.rectangle)
                self.mon_vaisseau.projectiles_vaisseau.remove(projec)


if __name__=="__main__":
    fenetre=Visuel()
    fenetre.title("Space Invader")
    fenetre.mainloop()

