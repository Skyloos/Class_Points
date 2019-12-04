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
        fichier = open("data.txt", 'a')
        fichier.write(str(self.name) + ": (" + str(self.x) + ";" + str(self.y) + ")\n")
        fichier.close()
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
                fichier.write("[" + other[point-1].name + other[point].name + "] = " + str(round(math.sqrt((other[point].x - other[point-1].x)**2 + (other[point].y - other[point-1].y)**2), 2)) + "\n")
            except IndexError:
                fichier.write("[" + self.name + other[point].name + "] = " + str(round(math.sqrt((self.x - other[point].x)**2 + (self.y - other[point].y)**2), 2)) + "\n")
            fichier.close()


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