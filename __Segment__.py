import __Point__ as cp
import os
import math

class Segment:
    def __init__(self, point1, point2):
        """
        Definit les caracteristiques du point dans "self"
        """
        self.point1 = point1
        self.point2 = point2
        self.x1, self.x2, self.y1, self.y2 = self.point1.x, self.point2.x, self.point1.y, self.point2.y
    def longueur(self):
        """
        Envoie la longueur du segment
        """
        longueur = round(math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2), 2)
        return longueur

if __name__ == "__main__":
    print("Lancement du module __classe__ en cours...")
    print("Fin du module.")
    while 1:
        os.system("pause")