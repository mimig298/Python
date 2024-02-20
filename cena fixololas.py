from random import randint
from time import sleep
caracteres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", "|", "!", '"', "@", "#", "£", "$", "§", "€", "%", "&", "/", "{", "(", "[", ")", "]", "=", "}", "'", "?", "«", "»", "+", "*", ",", ";", ".", ":", "-", "_", "<", ">"]

msg = input("Diz uma cena qualquer idk: ")
print()

for x in range(len(msg)):
    omgs = ""
    for y in range(x+1):
        omgs = omgs + caracteres[randint(0, len(caracteres)-1)]
    print(omgs)
    sleep(0.02)
for x in range(len(msg)+1):
    omgs = msg[:x]
    for y in range(len(msg)-x):
        omgs = omgs + caracteres[randint(0, len(caracteres)-1)]
    print(omgs)
    sleep(0.05)

input()