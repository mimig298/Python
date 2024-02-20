import random

def geracao(individuoA, individuoB):
    filhos = []
    for x in range (random.randint(2,5)):
        filho = round(((individuoA + individuoB) / 2) * (random.randint(4, 14)/10))
        filhos.append(filho)
    return filhos

individuoA = random.randint(50, 150)
individuoB = random.randint(50, 150)
evolucao = []
while True:
    individuos = geracao(individuoA, individuoB)
    evolucao.append(round(sum(individuos)/len(individuos), 1))
    print("As médias de pontuação de filhos até agora foram", evolucao)
    print("Os filhos são", individuos)
    individuoA = individuos[int(input("Pessoa A: "))-1]
    individuoB = individuos[int(input("Pessoa B: "))-1]
    print()
    