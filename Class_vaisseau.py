class Vaisseau:
    def __init__(self,canvas):
        self.canvas=canvas
        self.x=350
        self.y=600
        self.v=1
        self.dt=8
        self.dx=1
        self.dy=0
        self.create()
        self.toucher_bordure()
        self.key_handler()

    def create(self):
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

class Alien:
    def __init__(self,canvas):
        self.canvas=canvas
        self.x=350
        self.y=600
        self.v=1
        self.dt=8
        self.dt2=15
        self.dx=1
        self.dy=0
        self.create()
        self.bouger()
        self.toucher_bordure()
        self.tir()

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

    def tir(self):
        coord=self.canvas.coords(self.rectangle)
        self.x=coord[0]
        Projectile(self.x + 25, self.y, self.canvas)
        self.canvas.after(self.dt2,self.tir)