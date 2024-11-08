#Importation de la librairie tkinter pour la partie visuelle de Space Invader
import tkinter as tk


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
        self.canvas1.create_image(300,300,anchor='center',image=self.image)

class Personnage:
    def __init__(self,canvas):
        self.canvas=canvas
        self.x=100
        self.y=100
        self.v=0
        self.create()

    def create(self):
        self.rectangle=self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50,fill='red')

if __name__=="__main__":
    fenetre=Visuel()
    fenetre.title("Space Invader")
    fenetre.mainloop()


            

