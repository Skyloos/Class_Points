"""
Ensemble des class utilisees dans __main__
"""
import turtle as ttl
import random as rd
import __function__ as fonc
import math

class Point:
    def __init__(self,name = "", x= 0, y= 0, masse= 1):
        """
        Definit les caracteristiques du point dans "self"
        """
        self.name = name
        self.x = x
        self.y = y
        self.masse = masse
    def random(self, nameList):
        """
        Redefinit les caracteristiques du point aleatoirement
        """ 
        nameNumber = rd.randint(0, len(nameList))
        del nameList[nameList.index(nameNumber)]
        self.name = nameList[nameNumber]
        self.x = rd.randint(-250,250)
        self.y = rd.randint(-250,250)
        self.masse = rd.randint(1,10)
        return(self)
    def tracer(self):
        """
        Trace le point dans le repere
        """
        tortue = fonc.tortue()
        tortue.speed("fastest")
        tortue.up()
        tortue.goto(self.x, self.y)
        tortue.dot(3)
        tortue.write(str(self.name) + "\n" + "(" + str(round(self.x, 1)) + ";" + str(round(self.y, 1)) + ")" + "\n" + "m = " + str(self.masse))
        tortue.down()
        fichier = open("data.txt", 'a')
        fichier.write(str(self.name) + ": (" + str(round(self.x, 1)) + ";" + str(round(self.y, 1)) + ")" + " m = " + str(self.masse) + "\n")
        fichier.close()
        tortue.ht()
    def liage(self, *other):
        """
        Relie les points dans l'ordre des arguments
        """
        other = list(other)
        if type(other[0]) == list:
            otherKick = list(other[0])
            del other[0]
            for element in otherKick:
                other.append(element)
            firstElement = other[0]
            del other[0]
            other.append(firstElement)
        tortue = fonc.tortue()
        tortue.speed("fastest")
        tortue.up()
        tortue.goto(self.x, self.y)
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
        tortue.ht()
    def milieu(self, dictMilieu, *other):
        """
        Cree un point M qui est le milieu de plusieurs points
        """
        other = list(other)
        if type(other[0]) == list:
            otherKick = list(other[0])
            del other[0]
            for element in otherKick:
                other.append(element)
            firstElement = other[0]
            del other[0]
            other.append(firstElement)
        Milieu_name = "M" + "[" + str(self.name) + str(other[0].name)
        Milieu_x = self.x + other[0].x
        Milieu_y = self.y + other[0].y
        for point in range(len(other)-1):
            Milieu_x += other[point+1].x
            Milieu_y += other[point+1].y
            Milieu_name += str(other[point+1].name)
        Milieu_x /= (len(other)+1)
        Milieu_y /= (len(other)+1)
        Milieu_name += "]"
        Milieu = Point(Milieu_name, Milieu_x, Milieu_y)
        dictMilieu[str(Milieu_name)] = Milieu
        Milieu.tracer()
        return Milieu 


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
    print("Fin du module.")