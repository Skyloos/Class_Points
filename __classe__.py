"""
Ensemble des class utilisees dans __main__
"""
import turtle as ttl
import random as rd
import __function__ as fonc
import math

class Point:
    def __init__(self,name = "", x= 0, y= 0):
        """
        Definit les caracteristiques du point dans "self"
        """
        self.name = name
        self.x = x
        self.y = y
    def random(self):
        """
        Redefinit les caracteristiques du point aleatoirement
        """
        self.name = chr(rd.randint(65,90))
        self.x = rd.randint(-250,250)
        self.y = rd.randint(-250,250)
    def tracer(self):
        """
        Trace le point dans le repere
        """
        tortue = fonc.tortue()
        tortue.up()
        tortue.goto(self.x, self.y)
        tortue.dot(3)
        tortue.write(str(self.name) + "\n" + "(" + str(self.x) + ";" + str(self.y) + ")")
        tortue.down()
        fichier = open("data.txt", 'a')
        fichier.write(str(self.name) + ": (" + str(self.x) + ";" + str(self.y) + ")\n")
        fichier.close()
    def liage(self, *other):
        """
        Relie les points dans l'ordre des arguments
        """
        tortue = fonc.tortue()
        tortue.up()
        tortue.goto(self.x, self.y)
        other = list(other)
        for point in range(len(other)):
            tortue.down()
            tortue.goto(other[point].x, other[point].y)
            tortue.up()
            fichier = open("data.txt", 'a')
            try:
                segment = Segment(other[point-1], other[point])
                fichier.write("[" + other[point-1].name + other[point].name + "] = " + str(segment.longueur()) + "\n")
            except IndexError:
                segment = Segment(self, other[point])
                fichier.write("[" + self.name + other[point].name + "] = " + str(segment.longueur()) + "\n")
            fichier.close()
    def milieu(self, *other):
        other = list(other)
        Milieu_x = (self.x + other[0].x) /2
        Milieu_y = (self.y + other[0].y) /2
        for point in range(len(other)-1):
            Milieu_x = (Milieu_x + other[point].x) / point
            Milieu_y = (Milieu_y + other[point].y) / point
        Milieu = Point("M", Milieu_x, Milieu_y)
        Milieu.tracer()


class Segment:
    def __init__(self, point1, point2):
        """
        Definit les caracteristiques du point dans "self"
        """
        self.point1 = point1
        self.point2 = point2
    def longueur(self):
        """
        Envoie la longueur du segment
        """
        longueur = round(math.sqrt((self.point1.x - self.point2.x)**2 + (self.point1.y - self.point2.y)**2), 2)
        return longueur


if __name__ == "__main__":
    print("Lancement du module __classe__ en cours...")
    fonc.repere(fonc.tortue())
    a = Point()
    a.random()
    a.tracer()
    b = Point()
    b.random()
    b.tracer()
    print("Fin du module.")