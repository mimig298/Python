from time import sleep
from random import randint

energmult = 1
color = 0, 0, 0

def setcolor(r, g, b):
    global color
    color = r, g, b
    printcolor(color)

def randcolor():
    return randint(0, 255), randint(0, 255), randint(0, 255)

def printcolor(color):
    r, g, b = color
    print(int(r*energmult), int(g*energmult), int(b*energmult))

def gradient(orig, final, fadetime):
    r1, g1, b1 = orig
    r2, g2, b2 = final
    for i in range(fadetime):
        r = r1+(r2-r1)/fadetime*(i+1)
        g = g1+(g2-g1)/fadetime*(i+1)
        b = b1+(b2-b1)/fadetime*(i+1)
        setcolor(r, g, b)
        sleep(0.05)

setcolor(255, 255, 255)
setcolor(0, 0, 0)
def loop():
    while True:
        gradient(color, randcolor(), 20)
        #print("--------------")
        
loop()
