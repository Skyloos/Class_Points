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

def dictionnary_milieu():
    """
    Cree un dictionnaire pour enregistrer les milieux sous la forme de {str(name): Point}
    """
    dictMilieu = {}
    return dictMilieu

if __name__ == "__main__":
    print("Lancement du module __fonction__ en cours...")
    tortue()
    repere(tortue())
    print("Fin du module.")