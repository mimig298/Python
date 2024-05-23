from time import sleep

def normalize(x, y):
    lenght = (x**2 + y**2)**0.5
    if lenght == 0:
        return 0, 0
    newx = x/lenght
    newy = y/lenght
    return newx, newy
