import __Point__ as cp
import __function__ as fonc
import turtle as ttl


class Fonction:
    def __init__(self, *coef):
        """
        """
        self.coef = coef

        chaine = ""
        for element in range(len(self.coef)):
            if element == 0:
                chaine += str(self.coef[element]) + "+"
            elif self.coef[element] < 0:
                chaine += "(" + str(self.coef[element]) + ")*x**" + str(element) + "+"
            else:
                chaine += str(self.coef[element]) + "*x**" + str(element) + "+"
        self.chaine = chaine[:-1]
    def __str__(self):
        chaine = ""
        for element in range(len(self.coef)):
            if element == 0:
                chaine += str(self.coef[element]) + "+"
            elif self.coef[element] < 0:
                chaine += "(" + str(self.coef[element]) + ")x**" + str(element) + "+"
            else:
                chaine += str(self.coef[element]) + "x**" + str(element) + "+"
        chaine = chaine[:-1]
        return chaine
    def y(self,x):
        """
        """
        if x < 0:
            x = "(" + str(x) + ")"
        return eval(self.chaine.replace("x", str(x)))
    def extremum(self):
        """
        Renvoie l'abscisse et l'ordonnee de l'extremum de la fonction
        """
        if "x**2" in self.chaine:
            alpha = (-self.coef[1])/(2*self.coef[2])
            strAlpha = "(" + str(alpha) + ")"
            beta = eval(self.chaine.replace("x", strAlpha))
            return (alpha, beta)
    def tracage(self, nameList):
        """
        Trace la fonction
        Non fini
        """
        if len(self.coef) == 1:
            tortue = fonc.turtue()
            tortue.up()
            tortue.goto(self.coef[0], self.y(self.coef[0]))
            tortue.down()
            tortue.ht()


if __name__ == "__main__":
    print("Lancement du module __Fonction__ en cours...")
    f = Fonction(0,1,1)
    print(f.y(f.extremum()[0]))
    print("Fin du module.")