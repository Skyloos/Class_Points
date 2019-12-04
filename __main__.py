import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())

a = cl.Point()
a.random()
a.tracer()

b = cl.Point()
b.random()
b.tracer()

c = cl.Point()
c.random()
c.tracer()

a.liage(b,c,a)

help(fonc)

while 1:
    os.system("pause")
