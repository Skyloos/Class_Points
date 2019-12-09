class Fonction:
    def __init__(self, *para):
        """
        """
        self.para = para

        chaine = ""
        for element in range(len(self.para)):
            if element == 0:
                chaine += str(self.para[element]) + "+"
            elif self.para[element] < 0:
                chaine += "(" + str(self.para[element]) + ")*x**" + str(element) + "+"
            else:
                chaine += str(self.para[element]) + "*x**" + str(element) + "+"
        self.chaine = chaine[:-1]
    def __str__(self):
        chaine = ""
        for element in range(len(self.para)):
            if element == 0:
                chaine += str(self.para[element]) + "+"
            elif self.para[element] < 0:
                chaine += "(" + str(self.para[element]) + ")x**" + str(element) + "+"
            else:
                chaine += str(self.para[element]) + "x**" + str(element) + "+"
        chaine = chaine[:-1]
        return chaine
    def y(self,x):
        if x < 0:
            x = "(" + str(x) + ")"
        return eval(self.chaine.replace("x", str(x)))
    def maxi(self):
        if "x**2" in self.chaine:
            alpha = (-self.para[1])/(2*self.para[2])
            strAlpha = "(" + str(alpha) + ")"
            beta = eval(self.chaine.replace("x", strAlpha))
            return (alpha, beta)


if __name__ == "__main__":
    print("Lancement du module __Fonction__ en cours...")
    f = Fonction(0,1,1)
    print(f.maxi()[0])
    print(f.y(f.maxi()[0]))
    print("Fin du module.")