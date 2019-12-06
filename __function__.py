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

if __name__ == "__main__":
    print("Lancement du module __fonction__ en cours...")
    nameList = liste_name(104)
    print(nameList)
    print("Fin du module.")