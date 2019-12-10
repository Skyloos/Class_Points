import __Point__ as cp
import __function__ as fonc
#import turtle as ttl
import os


class Fonction:
    def __init__(self, *coef):
        self.coef = coef

        chaine = ""
        for element in range(0, len(self.coef)):
            i =  -(element-(len(self.coef)-1)) 
            if element == len(self.coef)-1:
                if self.coef[element] < 0:
                    chaine += "(" + str(self.coef[element]) + ")"
                else:
                    chaine += str(self.coef[element])
            elif self.coef[element] < 0:
                chaine += "(" + str(self.coef[element]) + ")*x**" + str(i) + "+"
            else:
                chaine += str(self.coef[element]) + "*x**" + str(i) + "+"
        self.chaine = chaine
    def __str__(self):
        chaine = ""
        for element in range(0, len(self.coef)):
            i =  -(element-(len(self.coef)-1)) 
            if element == len(self.coef)-1:
                if self.coef[element] < 0:
                    chaine += "(" + str(self.coef[element]) + ")"
                else:
                    chaine += str(self.coef[element])
            elif self.coef[element] < 0:
                chaine += "(" + str(self.coef[element]) + ")x**" + str(i) + "+"
            else:
                chaine += str(self.coef[element]) + "x**" + str(i) + "+"
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
    f = Fonction(2,-2,-10)
    print(f)
    print("Fin du module.")
    while 1:
        os.system("pause")