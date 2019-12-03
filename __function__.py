"""
Ensemble des fonctions utilisées dans __main__
"""
import turtle as ttl

def repere():
    """
    Trace un repère orthonormé
    """
    ttl.up()
    ttl.goto(0,100)
    ttl.down()
    ttl.home()
    ttl.goto(100,0)
    ttl.up()

def clear_data():
    """
    Efface les données écrites dans le fichier "data.txt"
    """
    fichier = open("data.txt", 'w')
    fichier.write("")
    fichier.close()

if __name__ == "__main__":
    print("Lancement du module __fonction__ en cours...")
    print("Fin du module.")