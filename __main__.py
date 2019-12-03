from time import sleep
import __function__  as fonc
import __classe__ as cl

fonc.clear_data()
fonc.repere()
a = cl.Point("A", 50, 50)
a.tracer()

while 1:
    sleep(1)
