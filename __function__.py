"""
Ensemble des fonctions utilisees dans __main__
"""
import turtle as ttl

def tortue():
    """
    Cree un tortue. C'est un lutin qui trace sur la fenetre
    """
    tortue = ttl.Turtle()
    return tortue

def repere(tortue):
    """
    Trace un repere orthonorme
    Argument:
        tortue : Lutin tracant sur la fenetre
    """
    tortue.up()
    tortue.goto(0,100)
    tortue.down()
    tortue.home()
    tortue.goto(100,0)
    tortue.up()

def clear_data():
    """
    Efface les donnees écrites dans le fichier "data.txt"
    """
    fichier = open("data.txt", 'w')
    fichier.write("")
    fichier.close()

def dictionnary_point():
    """
    Cree un dictionnaire pour enregistrer les points sous la forme de {str(name): Point}
    """
    dictPoint = {}
    return dictPoint

def dictionnary_vecteur():
    """
    Cree un dictionnaire pour enregistrer les vecteurs sous la forme de {str(name): Vecteur}
    """
    dictVecteur = {}
    return dictVecteur

def liste_name(number):
    """
    Cree une liste de noms de points en fonction de number qui est le nombre de noms qui sera mis dans la liste
    """
    nameList = [i for i in range(number)]
    interList = []
    for element in nameList:
        i = 0
        while element > 25:
            element -= 26
            i += 1
        element = chr(element+65) + str(i)
        interList.append(element)
    nameList = interList
    return nameList

def int_decimal(number):
    """
    Permet de transformer un float en int ssi les decimales sont egales à 0
    """
    strNumber = str(number)
    if int(strNumber[strNumber.index('.')+1:]) == 0:
        return int(strNumber[:strNumber.index('.')])
    else:
        return number

if __name__ == "__main__":
    print("Lancement du module __function__ en cours...")
    print(int_decimal(2.004))
    print("Fin du module.")