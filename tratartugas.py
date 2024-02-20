import turtle

def gerador(nome, cor="green", tamanho=3, penCor="black"):
    nome = turtle.Pen()
    nome.shape = "turtle"
    nome.shapesize = tamanho
    nome.shapecolor = cor
    nome.color = penCor
    return nome