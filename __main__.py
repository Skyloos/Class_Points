import __function__  as fonc
import __classPoint__ as cp
import os
import random as rd

fonc.clear_data()
fonc.repere(fonc.tortue())
dictPoint = fonc.dictionnary_point()
nameList = fonc.liste_name(10)

liste = []
for point in range(10):
    print(nameList)
    p = cp.Point(dictPoint)
    #p.random_name(nameList, dictPoint)
    p.random(nameList, dictPoint)
    p.tracer("N")
    liste.append(p)


if len(liste) == 1:
    liste[0].liage(liste)
    liste[0].milieu(dictPoint, "N", liste)
else:
    liste[0].liage(liste[1:len(liste)], liste[0])
    liste[0].milieu(dictPoint, "N", liste[1:])


while 1:
    os.system("pause")
