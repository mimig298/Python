lenght = int(input("How much do you want to walk? "))

path = [" "]*lenght
pos = 0

while pos < lenght:
    path[pos-1] = " "
    path[pos] = "☺"
    bit = ""
    for thing in path:
        bit = bit + thing
    print(bit)
    print("Press ENTER to walk 1 space")
    input()
    pos += 1
print("Congratualtions! You won!")
input()