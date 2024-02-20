from time import sleep

money = 0
unlocks = {"shop":False, "shopAccessed":False}
shopItems = [["Value", "You get 1 more money per A", "20"]]

def mainPage():
    pass

def Shop():
    global money
    
    print("Here are the items you can buy:\n")
    for num in range(len(shopItems)):
        print(f"({num}) - {shopItems[num][0]}")

while True:
    if money >= 50:
        unlocks["shop"] = True
    
    print("\n")
    if unlocks["shop"]:
        print("[Shop", end="")
        print("]")
    print(f"You have {money} money.")
    if money <= 5:
        print("Press 'A' and 'Enter' to get more money.")
    elif money >= 50 and not unlocks["shopAccessed"]:
        print("Press 'S' and 'Enter' to access the shop.")
    else:
        print()
    print()
    
    a = input().upper()[0]
    if a == "A":
        money += 1
    elif a == "S":
        print("\n")
        Shop()