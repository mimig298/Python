from Vector import *
from time import sleep

projpos = Vector2(1080, 964)
enempos = Vector2(982, 984)
velocity = Vector2(3, 4)
maxspeed = 4

dist = Vector2(999, 999)
while dist.lenght() > 1:
    dist = enempos - projpos
    velocity *= 0.99
    velocity += dist.normalize() / 20
    if velocity.lenghtsquared() > maxspeed**2:
        velocity = velocity.normalize() * maxspeed
    
    projpos += velocity
    
    print(round(projpos, 2), round(velocity, 2), round(dist.lenght(), 2), round(velocity.lenght(), 2))
    sleep(0)
