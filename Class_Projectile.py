import tkinter as tk

class Projectile(x,y,personnage,niveau,fenetre):
    def __init__(self,personnage,niveau):
        if niveau==1:
            dy=20
        elif niveau==2:
            dy=50
        if personnage==alien and niveau>0:
            dy=-dy
        Projectile= fenetre.Canevas.create_oval(x-50,y-50,width=1,outline='white',fill='blue')
    def déplacement(Projectile):
        if y>hauteur or y<-hauteur:
            Projectile.tk.destroy()
            return
        if 
        fenetre.after(20,déplacement)
        