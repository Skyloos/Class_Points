import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())

a = cl.Point("A", -100, -100)
a.tracer()

b = cl.Point("B", 100, -100)
b.tracer()

c = cl.Point("C", 100, 100)
c.tracer()

d = cl.Point("D", -100, 100)
d.tracer()

a.liage(b,c,d,a)
a.milieu(b,c,d)

while 1:
    os.system("pause")
