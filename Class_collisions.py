#Fait par Calisto Del Aguila et Bilel Ghouaiel
#implémentation de la classe Collisions du space invader
# #Fait le 18 novembre 2024
# A améliorer: l'algorithme d'apparition des aliens
# A ajouter: l'image des projectiles


import tkinter as tk


class Collisions:           
    #classe qui gère l'ensemble des collisions entre les projectiles et les vaisseaux et aliens
    def __init__(self, canvas, vaisseau, liste_aliens):

        self.canvas = canvas
        self.vaisseau = vaisseau #le vaisseau est le joueur
        self.liste_aliens = liste_aliens #liste contenant les aliens dont on va vérifier la position
        self.col()

    def col(self):
        #fonction qui gère l'ensemble des collisions aliens et vaisseau

        self.detect_vaisseau_projectiles()
        self.detect_aliens_projectiles()
        self.canvas.after(50, self.col)

    def detect_vaisseau_projectiles(self):
        #fonction qui détecte si il y a collisions entres les projectiles et le vaisseau

        for projectile in self.vaisseau.Liste_Projectile[:]:

            for alien in self.liste_aliens[:]:

                if self.detect_collision(projectile.circle, alien.rectangle):
                    alien.vie -= projectile.degat
                    self.canvas.delete(projectile.circle)
                    self.vaisseau.Liste_Projectile.remove(projectile)

                    if alien.vie <= 0:
                        #supprime l'alien si il n'a plus de vie
                        self.canvas.delete(alien.rectangle)
                        self.liste_aliens.remove(alien)

    def detect_aliens_projectiles(self):
        #fonction qui détecte si il y a collisions entre les projectiles et les aliens
        
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
        #fonction qui détecte la collision ou si un projectile passe proche d'un alien ou du vaisseau
        
        bbox1 = self.canvas.bbox(obj1)
        bbox2 = self.canvas.bbox(obj2)
        if not bbox1 or not bbox2:
            return False
        return not (bbox1[2] < bbox2[0] or bbox1[0] > bbox2[2] or
                    bbox1[3] < bbox2[1] or bbox1[1] > bbox2[3])
        