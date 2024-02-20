from random import randint

pessoas = ["José", "Maria", "André", "Joaquim", "Francisco", "Margarida", "Inês", "Sofia", "Jaime", "Andreia", "Paula", "Gonçalo", "Martim", "Xavier", "Susana", "Leonor", "Mariana", "Leonardo", "Miguel", "Ricardo", "João", "Filipa", "Filipe", "Frederico", "Isabel", "Pedro", "Paulo", "Rafael", "Afonso", "Joana", "Márcia", "Nuno", "Raquel", "Beatriz", "Bernardo"]

def listItem(sList):
    return sList[randint(0, len(sList)-1)]

frases = ["/pessoa casou com /pessoa", "/pessoa convidou /pessoa e /pessoa para uma festa", "/pessoa e /pessoa tiveram uma discussão", "/pessoa não deu os parabéns a /pessoa", "/pessoa bloqueou /pessoa", "/pessoa estava a discutir com /pessoa mas /pessoa moderou a situação", "/pessoa está a namorar com /pessoa , deixando /pessoa com ciúmes", "/pessoa e /pessoa já não são amigos", "Como /pessoa não gosta de /pessoa , /pessoa cortou-lhe relações", "/pessoa e /pessoa são agora melhores amigos", "/pessoa deixou /pessoa para namorar com /pessoa"]

def criaFrase():
    frase = listItem(frases)
    fraseP = frase.split(" ")
    for x in range(len(fraseP)):
        if fraseP[x] == "/pessoa":
            fraseP[x] = listItem(pessoas)
    frase = ""
    for palavra in fraseP:
        if palavra != ",":
            frase = frase + " " + palavra
        else:
            frase = frase + ","
    frase = frase[1:len(frase)] + "."
    return frase

for x in range(10):
    print(criaFrase())
input()