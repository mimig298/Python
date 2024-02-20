from math import log10, floor
from time import sleep

numero = 1
letras = ["k", "M", "B", "T", "Qa", "Qt", "Sx", "St", "Oc", "No", "Dc"]

def convert(numero):
    notas = "k"*floor(log10(numero)/3)
    for x in range(len(letras)):
        while letras[x]*2 in notas:
            notas = notas.replace(letras[x]*2, letras[x+1])
    return notas

for x in range(82946328756328573):
    numero = numero * 10
    print("10^", floor(log10(numero)), "é o mesmo que", convert(numero))