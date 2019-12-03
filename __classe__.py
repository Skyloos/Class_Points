"""
Ensemble des class utilisées dans __main__
"""
import turtle as ttl
import random as rd
import __function__ as fonc

class Point:
    def __init__(self,name = "", x= 0, y= 0):
        """
        Définit les caractéristiques du point dans "self"
        """
        self.name = name
        self.x = x
        self.y = y
        fichier = open("data.txt", 'a')
        fichier.write(str(self.name) + ": (" + str(self.x) + ";" + str(self.y) + ")\n")
        fichier.close()
    def random(self):
        """
        Redéfinit les caractéristiques du point aléatoirement
        """
        self.name = chr(rd.randint(65,90))
        self.x = rd.randint(-400,400)
        self.y = rd.randint(-400,400)
    def tracer(self):
        """
        Trace le point dans le repère
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
                fichier.write("[" + other[point-1].name + other[point].name + "]" + "\n")
            except IndexError:
                fichier.write("[" + self.name + other[point].name + "]" + "\n")
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