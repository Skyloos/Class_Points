import turtle

class Point:
    def __init__(self,name = "", x= 0, y= 0):
        """
        Définit les caractéristiques du point dans "self"
        """
        self.name = name
        self.x = x
        self.y = y
        fichier = open("data.txt", 'a')
        fichier.write(str(self.name), ": (", str(self.x), ";", ")\n")
        fichier.close()
    def tracer(self):
        """
        Trace le point dans le repère
        """
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.dot(3)
        turtle.write(str(self.name), "\n", "(", str(self.x), ";", str(self.y), ")")
        turtle.down()

if __name__ == "__main__":
    a = Point("A", 50, 50)