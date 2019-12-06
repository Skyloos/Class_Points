import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())
dictPoint = fonc.dictionnary_point()
nameList = fonc.liste_name(3)

liste = []
for point in range(3):
    p = cl.Point(dictPoint)
    p.random(nameList, dictPoint)
    p.tracer("N")
    liste.append(p)


if len(liste) == 1:
    liste[0].liage(liste)
    liste[0].milieu(liste)
else:
    liste[0].liage(liste[1:len(liste)], liste[0])
    liste[0].barycentre(dictPoint, liste[1:])

print(dictPoint)

while 1:
    os.system("pause")
