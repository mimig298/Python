from time import sleep
from random import randint

pos = 0
vel = 0
acc = 0

while True:
    acc += randint(-4, 4)
    if pos > acc:
        acc -= 1
    elif pos < -acc:
        acc += 1
    vel = round(vel+acc/100, 2)
    pos = round(pos+vel/10, 2)
    print(pos, vel, acc)
    sleep(0.05)
    