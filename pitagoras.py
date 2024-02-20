from math import sqrt

a = 0
r = 0
while a != "CC" and a != "CH":
    a = input("Queres calcular a hipotenusa com os dois catetos ou um cateto com a hipotenusa e um cateto? [CC/CH]: ").upper()
while r != "N" and r != "D" and r != "C":
    r = input("Queres arredondar? Se sim, às décimas ou centenas? [n/d/c]: ").upper()

if a == "CC":
    c1 = float(input("Primeiro cateto: "))
    c2 = float(input("Segundo cateto: "))
    hp = sqrt(c1**2 + c2**2)
    if r == "D":
        hp = round(hp, 1)
    elif r == "C":
        hp = round(hp, 2)
    print("A hipotenusa desse triângulo é", hp)
else:
    c1 = float(input("Cateto: "))
    hp = float(input("Hipotenusa: "))
    c2 = sqrt(hp**2 - c1**2)
    if r == "D":
        hp = round(c2, 1)
    elif r == "C":
        hp = round(c2, 2)
    print("O outro cateto desse triângulo é", c2)
    
input()