from time import sleep

projframes = 4
framecounter = 0
frame = 0

while True:
    if framecounter + 1 >= 5:
        framecounter = 0
        frame = (frame+1)%projframes
    framecounter += 1
    
    print(frame, framecounter)
