from time import sleep
from os import system

mb = 2.19*1024
mbP = 0
gbP = 0
percP = 0
max = 15479

while mb < max:
    mb += 1
    perc = round(mb*100/max, 1)
    if mb > 1500:
        gb = round(mb/1024, 2)
        if gbP != gb or percP != perc:
            system("cls")
            print(gb, "GB  ", perc, "%")
            gbP = gb
            percP = perc
    else:
        system("cls")
        print(mb, "MB  ", perc, "%")
        percP = perc
    sleep(0.01)