from random import randint

# Sílabas possíveis num MegAmogus
silabas = ["mo", "mo", "ma", "ga", "go", "gu"]

# Quão grande é o MegAmogus
lenght = int(input("Quantas sílabas tem o MegAmogus?\n>>> "))

# Gerar o MegAmogus
def criaMogus(lenght):
    megamogus = "a" # começa sempre com a
    if lenght > 0:
        megamogus = megamogus + silabas[randint(1, 2)] # a sílaba seguinte é sempre ma ou mo
    for x in range(lenght-1):
        megamogus = megamogus + silabas[randint(0, len(silabas)-1)] # preencher o resto da palavra
    megamogus = megamogus + "mogus" # acaba sempre com mogus
    return megamogus

#Dá uns quantos MegAmogus
print()
for x in range(5):
    print(criaMogus(lenght))
input()