from turtle import up, goto, down, home
from time import sleep

class Point:
    def __init__(self,name = "", x= 0, y= 0):
        """
        Définit les caractéristiques du point dans "self"
        """
        self.name = name
        self.x = x
        self.y = y
    def tracer(self):
        """
        Trace le point dans le repère
        """
        up()
        goto(self.x, self.y)
        down()
        
def repere():
    """
    Trace un repère orthonormé
    """
    up()
    goto(0,100)
    down()
    home()
    goto(100,0)
    up()
        
repere()

while 1:
    sleep(1)
