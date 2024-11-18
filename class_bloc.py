import tkinter as tk

class bloc(x,fenetre):

    def __init__(self):
        self.x=x
        self.y = canvas_height = self.canvas.winfo_height() - 50
        self.create()
    
    def create(self):
        self.rectangle=self.canvas.create_rectangle(self.x, self.y, self.x + 50, self.y + 50,fill='red')
    