import time

text = "a"

for x in range(int(1.79*(10**308))):
    space = 10
    spaces = "          "
    negative = 0
    for hey in range(x):
        if hey - negative > 10:
            spaces = spaces + text
            negative += 10
        else:
            spaces = " " + spaces
    print(spaces + text)