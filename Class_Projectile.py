import tkinter as tk

class Projectile:
    def __init__(self,x,y,canvas):
        self.x = x
        self.y = y
        self.dy = -8
        self.canvas=canvas
        self.create()
        self.bouger()
    

    def create(self):
        self.circle=self.canvas.create_oval(self.x + 5 , self.y + 5 , self.x - 5 , self.y - 5 ,fill='white')
    

    def bouger(self):
        "self.canvas.move(self.circle, self.dx, self.dy)"
        "if camp(self)==ennemi:"
        "self.dy = -self.dy"
        self.dt=38
        self.y += self.dy
        self.canvas.move(self.circle,0,self.dy)
        self.canvas.after(self.dt, self.bouger)

        self.toucher_bordure()
    
    
    def toucher_bordure(self):
        canvas_height = self.canvas.winfo_height()  # Hauteur du canevas

        # Vérifie si le projectile touche les bords haut ou bas
        if self.y <= 0 or self.y + 8 >= canvas_height:
            self.canvas.delete(self.circle)
