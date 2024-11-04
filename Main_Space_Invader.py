import tkinter as tk


class Visuel(tk.Tk):
    def __init__(self,):
        tk.Tk.__init__(self)
        self.image=tk.PhotoImage(file="Espace.gif")
        self.Boutton()
        self.menu()
        self.canvas()
    def Boutton(self):
        self.JeuButton=tk.Button(self,text='Jouer')
        self.QuitButton=tk.Button(self,text='Quitter',command=self.destroy)
        self.QuitButton.pack()
        self.JeuButton.pack()
    def menu(self):
        self.menubar=tk.Menu(self)
        self.menu1=tk.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Menu',menu=self.menu1)
        self.menu1.add_command(label="A propos")
        self.config(menu=self.menubar)
    def canvas(self):
        
        self.canvas1=tk.Canvas(self,width= 800, height=700, bg='blue')
        self.canvas1.pack()
        self.canvas1.create_image(300,300,anchor='center',image=self.image)

if __name__=="__main__":
    fenetre=Visuel()
    fenetre.title("Space Invader")
    fenetre.mainloop()
            