import time

coisas = ["m", "b", "tr", "quadr", "quint", "sext", "sept", "oct", "non", "dec"]
numero = 1000

print("Vives nos Estados Unidos ou no Brazil? [S/N]")
coisa = input()
print()

for x in range(10):
    if coisa.upper() == "S":
        numero = numero * 1000
    else:
        numero = numero ** 2
    if x > 0 and coisa.upper() != "S":
        print(str(numero) + " = 1 " + coisas[x] + "ilião")
    elif x == 0 or coisa.upper() == "S":
        print(str(numero) + " = 1 " + coisas[x] + "ilhão")
    time.sleep(1)
    print()