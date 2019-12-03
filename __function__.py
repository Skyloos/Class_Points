from turtle import up, goto, down, home

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

if __name__ == "__main__":
    repere()