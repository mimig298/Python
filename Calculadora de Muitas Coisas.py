primes = [2, 3, 5, 7]

def findDivisores(number):
    divisores = []
    for x in range(1, int(abs(number/2))+1):
        #print("Checking if", number, "is divisible by", x)
        if x > number/2:
            break
        if x in divisores:
            break
        if number % x == 0:
            divisores.append(x)
            if not int(number/x) in divisores:
                divisores.append(int(number/x))
        #for x in range(1, int(abs(number))):
            #if number % (x+1) == 0:
                #divisores.append(x+1)
    if not number in divisores:
        divisores.append(number)
    return sorted(divisores)

def mdc(n1, n2):
    divN1 = findDivisores(n1)
    divN2 = findDivisores(n2)
    comuns = []
    for x in divN1:
        if x in divN2:
            comuns.append(x)
    return comuns[len(comuns)-1]

def isPrime(number):
    if number % 2 == 0 and number != 2:
        return False
    if len(findDivisores(number)) == 2:
        return True
    else:
        return False

def findPrimes(maxN):
    minN = primes[len(primes)-1]
    if minN >= maxN+1:
        return "Already checked"
    for x in range(maxN+1-minN):
        #print("Checking if", minN+x+1, "is prime...")
        if isPrime(minN+x+1):
            primes.append(minN+x+1)
    return "Added prime numbers to list"

def fatoriza(n):
    fatores = []
    while n != 1:
        divide = 0
        while n % primes[divide] != 0:
            #print("Attempting to divide", n, "by", primes[divide], "...")
            divide += 1
            if divide >= len(primes):
                #print("Couldn't divide", n, "by any prime currently known. Updating primes list to up to", n, "...")
                findPrimes(n)
                #print("Added all prime numbers up to", n)
        fatores.append(primes[divide])
        #print(n, "can be divided by", primes[divide], "!")
        n = int(n/primes[divide])
    return fatores

def tornaIrredutivel(f):
    f = f.split("/")
    f[0] = int(f[0])
    f[1] = int(f[1])
    mdcND = mdc(f[0], f[1])
    f[0] = int(f[0]/mdcND)
    f[1] = int(f[1]/mdcND)
    irrF = str(f[0]) + "/" + str(f[1])
    return irrF

def tornaDecimal(f):
    f = f.split("/")
    f[0] = int(f[0])
    f[1] = int(f[1])
    fatoresDen = fatoriza(f[1])
    nao52 = []
    for x in fatoresDen:
        if x != 2 or x != 5:
            nao52.append(x)
    if len(nao52) >= 1:
        fatoresNum = fatoriza(f[0])
        for x in nao52:
            if x in fatoresNum:
                fatoresNum.remove(x)
                f[0] = int(f[0] / x)
                f[1] = int(f[1] / x)
            else:
                return False
        fatoresDen = fatoriza(f[1])
    return "deez nutz"

def period2fracao(n):
    pass

print("Bem vindo/a à Calculadora de Muitas Coisas!")
print("Este programa premite-te calcular coisas que uma calculadora normal não consegue.")

while True:
    print("Estas são todas as funções que a CMC tem até agora, e mais vão ser adicionadas ao longo do tempo:")
    print("""
    1 - Listar divisores de um número
    2 - Descobrir o MDC de 2 números
    3 - Descobrir o MMC de 2 números
    4 - Descobrir se um número é primo
    5 - Dividir um número em fatores primos
    6 - Tornar fração irredutível
    7 - Converter fração em fração decimal
    8 - Converter dízima infinita periódica em fração
    9 - Simplificar radical 
    """)
    answr = input("Insere o número correspondente à função que queres utilizar\n>>> ")
    print()
    
    a = 0
    if answr == "n":
        break
    while a != "n":
        if answr == "1":
            a = input("De que número queres saber os divisores?\n>>> ")
            if a == "n":
                break
            print()
            l_divisores = findDivisores(int(a))
            print("Os divisores de", a, "são:")
            for x in l_divisores:
                print(x)
            input()
        
        elif answr == "2":
            n1 = input("Qual é o primeiro número?\n>>> ")
            if n1 == "n":
                break
            n2 = input("Qual é o segundo número?\n>>> ")
            if n2 == "n":
                break
            print()
            Mindc = mdc(int(n1), int(n2))
            print("O MDC de", n1, "e", n2, "é", Mindc)
            input()
        
        elif answr == "4":
            a = input("Que número queres descobrir se é primo?\n>>> ")
            if a == "n":
                break
            print()
            if isPrime(int(a)):
                print(a, "é primo.")
            else:
                print(a, "não é primo.")
            input()
            
        elif answr == "5":
            a = input("Que número queres fatorizar em primos?\n>>> ")
            if a == "n":
                break
            fatores = fatoriza(int(a))
            numero = int(a)
            print()
            for fator in fatores:
                print(" "*(len(a)-len(str(numero))) + str(numero) + " | " + str(fator))
                numero = int(numero / fator)
            print(" "*(len(a)-1) + "1 |\n")
            input()
        
        elif answr == "6":
            a = input("Que fração queres tornar irredutível?\nExemplo de formatação: 3/4\n>>> ")
            if a == "n":
                break
            print()
            irredutivel = tornaIrredutivel(a)
            print(a, "na sua forma irredutível é", irredutivel)
            input()
        
        else:
            print("Função inválida!")
            input()
            break
    
    print()