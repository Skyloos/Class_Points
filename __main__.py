import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())

liste = []
for point in range(10):
    p = cl.Point()
    p.random()
    p.tracer()
    liste.append(p)


liste[0].liage(liste[1:-1])
liste[0].milieu(liste[1:])

while 1:
    os.system("pause")
