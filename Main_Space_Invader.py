#Importation de la librairie tkinter pour la partie visuelle de Space Invader
import tkinter as tk
from Class_Projectile import Projectile

class Visuel(tk.Tk):
#Cette classse s'occupe de créer toute la partie graphique/visuelle de Space Invader
    def __init__(self):
        tk.Tk.__init__(self)         #Création de la fenêtre de jeu
        self.image=tk.PhotoImage(file="Espace.gif")
        self.label()
        self.Boutton()
        self.menu()
        self.canvas()
        self.personnage = Personnage(self.canvas1)

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



class Personnage:
    def __init__(self,canvas):
        self.canvas=canvas
        self.x=350
        self.y=600
        self.v=1
        self.dt=8
        self.dx=1
        self.dy=0
        self.create()
        "self.bouger()"
        self.toucher_bordure()
        self.key_handler()

    def create(self):
        self.rectangle=self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50,fill='red')

    def bouger(self):
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

    def key_handler(self):
        self.canvas.bind("<Right>", self.Right)
        self.canvas.bind("<Left>", self.Left)
        self.canvas.bind("<space>",self.tir)
        self.canvas.focus_set()    
        
    def Left(self,event):
        x=-50
        y=0
        self.canvas.move(self.rectangle,x,y)
    
    def Right(self,event):
        x=50
        y=0
        self.canvas.move(self.rectangle,x,y)
    
    def tir(self,event):
        coord=self.canvas.coords(self.rectangle)
        self.x=coord[0]
        Projectile(self.x + 25, self.y, self.canvas)



if __name__=="__main__":
    fenetre=Visuel()
    fenetre.title("Space Invader")
    fenetre.mainloop()

