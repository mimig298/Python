from math import floor, pi
from Vector import Vector2, degrees

playerpos = Vector2(0, 0)
enempos = Vector2(8, 26)
enemvel = Vector2(-1, -5)
projspeed = 3

angle = "sup meu man bro"

found = False
frames = 0
prevreq = 0
while not found and frames < 100:
    epos = enempos + enemvel * frames
    dist = epos - playerpos
    reqframes = floor(dist.lenght()/projspeed)
    #if prevreq < frames <= reqframes:
    if reqframes == frames:
        angle = dist.torotation()
        found = True
    frames += 1
    prevreq = reqframes

print(degrees(angle), frames-1)

for tick in range(frames+1):
    epos = enempos + enemvel * tick
    ppos = playerpos + Vector2(0, projspeed).rotatedby(angle) * tick
    dist = (epos - ppos).lenght()
    print(round(epos), round(ppos), dist)