from time import sleep
import __function__  as fonc
import __classe__ as cl
import os

fonc.clear_data()
fonc.repere(fonc.tortue())
a = cl.Point("A", 50, 50)
a.tracer()

while 1:
    os.system("pause")
