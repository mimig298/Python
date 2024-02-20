from random import randint

# id, name, weight
items = [[0, "Common", 500], [1, "Uncommon", 200], [2, "Rare", 70], [3, "Ultra Rare", 10], [4, "Legendary", 5], [5, "Ultimate", 1]]

def Setup(iList):
    total = 0
    preTotal = 0
    area = []
    for item in iList:
        total += item[2]
        area.append([item[0], [preTotal+1, total]])
        preTotal = total
    return total, area

def GetItem(itemN, tList):
    out = randint(1, itemN)
    result = 0
    for item in tList:
        if out >= item[1][0] and out <= item[1][1]:
            result = item[0]
            break
    return result

total, nList = Setup(items)
tests = 100000
outcomes = [0, 0, 0, 0, 0, 0]
for x in range(tests):
    result = GetItem(total, nList)
    #print("You got " + items[result][1] + "!")
    outcomes[result] += 1
    
chances = {}
for x in range(len(outcomes)):
    chances[items[x][1]] = round(outcomes[x]*100/tests, 2)