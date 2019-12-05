import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())
dictMilieu = fonc.dictionnary_milieu()

liste = []
for point in range(10):
    p = cl.Point()
    p.random(fonc.liste_name(26))
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
    liste[0].milieu(dictMilieu, liste[1:])
"""
a = cl.Point()
a.random()
a.tracer()

b = cl.Point()
b.random()
b.tracer()

a.liage(b)
"""
print(dictMilieu)
while 1:
    os.system("pause")
