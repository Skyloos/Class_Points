import __Point__ as cp
import __function__ as fonc
#import turtle as ttl
import os


class Fonction:
    def __init__(self, *coef):
        self.coef = coef

        chaine = ""
        for element in range(len(self.coef)):
            element -= len(self.coef) - 1
            if element == 0:
                chaine += str(self.coef[element-1])
            elif self.coef[element] < 0:
                chaine += "(" + str(self.coef[element-1]) + ")*x**" + str(element*(-1)) + "+"
            else:
                chaine += str(self.coef[element-1]) + "*x**" + str(element*(-1)) + "+"
        self.chaine = chaine
    def __str__(self):
        chaine = ""
        for element in range(-len(self.coef), 0):
            i = element * (-1)
            i -= 1
            print(element)
            if element == 0:
                chaine += str(self.coef[element])
            elif self.coef[element] < 0:
                chaine += "(" + str(self.coef[element]) + ")x**" + str(element) + "+"
            else:
                chaine += str(self.coef[element]) + "x**" + str(element) + "+"
        return chaine
    def y(self,x):
        """
        Renvoie l'ordonnee de la fonction avec comme paramètre x etant definit dans l'argument
        """
        if x < 0:
            x = "(" + str(x) + ")"
        print(self.chaine.replace("x", str(x)))
        return eval(self.chaine.replace("x", str(x)))
    def x(self,y):
        """
        Renvoie l'abscisse de la fonction avec comme paramètre y (donc f(x)) etant definit dans l'argument
        Non fini
        """
        if len(self.coef) == 2:
            return eval("("+"(-" + str(self.coef[1]) +")+"+ "("+str(y)+")" + ")/("+ str(self.coef[0]) +")")
    def extremum(self):
        """
        Renvoie l'abscisse et l'ordonnee de l'extremum de la fonction
        """
        if "x**2" in self.chaine:
            alpha = (-self.coef[1])/(2*self.coef[0])
            strAlpha = "(" + str(alpha) + ")"
            beta = eval(self.chaine.replace("x", strAlpha))
            return (alpha, beta)
    def tracage(self):
        """
        Trace la fonction
        Non fini
        """
        if len(self.coef) == 2:
            tortue = fonc.tortue()
            tortue.up()
            tortue.goto(-180, self.y(-180))
            tortue.down()
            tortue.goto(180, self.y(180))
            tortue.ht()
        else:
            tortue = fonc.tortue()
            tortue.up()
            for i in range(-180,180):
                tortue.down()
                tortue.goto(i, self.y(i))
                tortue.ht()
            tortue.up()



if __name__ == "__main__":
    print("Lancement du module __Fonction__ en cours...")
    fonc.repere(fonc.tortue())
    f = Fonction(2,-2,0)
    print(f)
    #f.tracage()
    print("Fin du module.")
    while 1:
        os.system("pause")