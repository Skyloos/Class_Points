import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())

liste = []
for point in range(3):
    p = cl.Point()
    p.random()
    p.tracer()
    liste.append(p)

if len(liste) == 1:
    liste[0].liage(liste)
    liste[0].milieu(liste)
else:
    liste[0].liage(liste[1:-2])
    liste[0].milieu(liste[1:])

while 1:
    os.system("pause")
