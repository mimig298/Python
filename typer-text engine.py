import time
import os

texto = input("Qual é o texto? ")
comprido = len(texto)

for caracter in range(comprido):
    os.system("cls")
    print(texto[0:caracter+1])
    if texto[caracter] == ".":
        time.sleep(0.2)
    elif texto[caracter] == "?" or texto[caracter] == "!":
        time.sleep(0.35)
    elif texto[caracter] == ",":
        time.sleep(0.1)
    elif texto[caracter] == " ":
        time.sleep(0.07)
    else:
        time.sleep(0.05)

input()