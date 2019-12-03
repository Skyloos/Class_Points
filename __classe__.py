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
        tortue.write(str(self.name)+ "\n" + "(" + str(self.x) + ";" + str(self.y) + ")")
        tortue.down()

if __name__ == "__main__":
    print("Lancement du module __classe__ en cours...")
    fonc.repere(fonc.tortue())
    a = Point("A", 50, 50)
    print("Fin du module.")