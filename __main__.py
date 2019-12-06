import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())
dictPoint = fonc.dictionnary_point()

liste = []
nameList = fonc.liste_name(10)
for point in range(10):
    p = cl.Point(dictPoint)
    p.random(nameList, dictPoint)
    p.tracer()
    liste.append(p)
"""
for element in range(len(liste)):
    liste[element].liage(liste)
"""
if len(liste) == 1:
    liste[0].liage(liste)
    liste[0].milieu(liste)
else:
    liste[0].liage(liste[1:len(liste)], liste[0])
    liste[0].milieu(dictPoint, liste[1:])
"""
a = cl.Point()
a.random()
a.tracer()

b = cl.Point()
b.random()
b.tracer()

a.liage(b)
"""
print(dictPoint)
while 1:
    os.system("pause")
