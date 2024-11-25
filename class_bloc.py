#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation de la classe bloc
#Fait le 18 novembre 2024
# A améliorer: inclure le bloc dans la classe personnage avec une vitesse nulle
# A ajouter: Ajouter le skin du bloc

import tkinter as tk

class bloc():

    def __init__(self,x,fenetre):
        self.x=x
        self.y = canvas_height = self.canvas.winfo_height() - 50
        self.create()
    
    def create(self):
        #fonction qui créée un bloc
        self.rectangle=self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50,fill='red')
    