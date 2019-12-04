import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())

a = cl.Point()
a.random()
a.tracer()

liste = []
for point in range(100):
    p = cl.Point()
    p.random()
    p.tracer()
    liste.append(p)


a.liage(liste, a)
a.milieu(liste)

while 1:
    os.system("pause")
