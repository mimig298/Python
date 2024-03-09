# program that generates a gradient

from random import randint
from time import sleep

# generate the first line
gradient = [[0]*30]

for x in range(1000-1):
    newLine = []
    for y in gradient[x]:
        newDigit = y
        chance = 1
        # a number is more likely to increase the more other numbers have increased already
        for z in gradient[x]:
            if z > newDigit:
                chance += 1
        if randint(1, 50) <= chance:
            newDigit += 1
        newLine.append(newDigit)
    gradient.append(newLine)

maxChar = len(str(max(gradient[len(gradient)-1])))
for x in range(len(gradient)):
    line = ""
    for y in gradient[x]:
        char = str(y)
        line = line + " "*(maxChar-len(char)) + char + " "
    print(line)
    sleep(0.01)