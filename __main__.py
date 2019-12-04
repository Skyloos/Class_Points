import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())

a = cl.Point()
a.random()
a.tracer()

b = cl.Point("B", 129, 42)
b.tracer()

c = cl.Point("C", -169, 93)
c.tracer()

a.liage(b,c,a)
c.milieu(b)

while 1:
    os.system("pause")
