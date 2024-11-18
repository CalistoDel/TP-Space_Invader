import tkinter as tk

class Projectile(x,y,fenetre):
    def __init__(self):
        self.x=x
        self.y=y
        self.dy=8
        self.canva=fenetre.canvas1
        self.create()
        self.bouger()
        self.collision()
        self.toucher_bordure()
    

    def create(self):
        self.circle=self.canva.create_circle(self.x + 5 , self.y + 5 , self.x - 5 , self.y - 5 ,fill='white')
    

    def bouger(self):
        self.canvas.move(self.rectangle, self.dx, self.dy)
        if camp(self)==ennemi:
            self.dy = -self.dy
        self.y += self.dy
    
    
    def toucher_bordure(self):
        canvas_height = self.canvas.winfo_height()  # Hauteur du canevas

        # Vérifie si le projectile touche les bords haut ou bas
        if self.y <= 0 or self.y + 8 >= canvas_height:
            self.destroy()
