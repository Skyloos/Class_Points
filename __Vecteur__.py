import math
import os

class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.norme = math.sqrt(self.x**2 + self.y**2)
    def produit_scalaire(self, other):
        produitScalaire = self.norme * other.norme * math.cos(53)