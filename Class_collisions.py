#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation de la classe Jeu du space invader
# #Fait le 18 novembre 2024
# A améliorer: l'algorithme d'apparition des aliens
# A ajouter: Gérer les interactions entre les projectils, les blocs et les personnages


import tkinter as tk


class Collisions:
    def __init__(self, canvas, vaisseau, liste_aliens):
        self.canvas = canvas
        self.vaisseau = vaisseau
        self.liste_aliens = liste_aliens
        self.col()

    def col(self):
        self.detect_vaisseau_projectiles()
        self.detect_aliens_projectiles()
        self.canvas.after(50, self.col)

    def detect_vaisseau_projectiles(self):
        for projectile in self.vaisseau.Liste_Projectile[:]:
            for alien in self.liste_aliens[:]:
                if self.detect_collision(projectile.circle, alien.rectangle):
                    alien.vie -= projectile.degat
                    self.canvas.delete(projectile.circle)
                    self.vaisseau.Liste_Projectile.remove(projectile)
                    if alien.vie <= 0:
                        self.canvas.delete(alien.rectangle)
                        self.liste_aliens.remove(alien)

    def detect_aliens_projectiles(self):
        for alien in self.liste_aliens:
            for projectile in alien.projectiles[:]:
                if self.detect_collision(projectile.circle, self.vaisseau.rectangle):
                    self.canvas.delete(projectile.circle)
                    alien.projectiles.remove(projectile)
                    self.vaisseau.vie -= projectile.degat
                    if self.vaisseau.vie <= 0:
                        print("Game Over!")
                        self.canvas.quit()

    def detect_collision(self, obj1, obj2):
        bbox1 = self.canvas.bbox(obj1)
        bbox2 = self.canvas.bbox(obj2)
        if not bbox1 or not bbox2:
            return False
        return not (bbox1[2] < bbox2[0] or bbox1[0] > bbox2[2] or
                    bbox1[3] < bbox2[1] or bbox1[1] > bbox2[3])
        