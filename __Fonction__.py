class Fonction:
    def __init__(self, *para):
        """
        """
        self.para = para
    def __str__(self):
        chaine = ""
        for element in range(len(para)):
            if element == 0:
                chaine += str(para[element])
            else:
                chaine += str(para[element]) + "**" + str(element) + "+"
        chaine = chaine[:-1]

if __name__ == "__main__":
    print("Lancement du module __Fonction__ en cours...")
    print("Fin du module.")