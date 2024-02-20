# Quantos itens?
print("Quantos itens?")
n_itens = int(input())

# Criar uma lista com todos os itens
itens = []
for item in range(n_itens):
    itens.append(item + 1)

# Por número de grupos ou itens em grupo?
print("Queres saber quantos itens por grupo ou quantos grupos por itens? [I/G]")
answer = input().lower()

# Decidir quantos itens/grupo se houver x grupos
if answer == "i":
    print("Quantos grupos há?")
    n_grupos = int(input())
    if n_itens % n
    IporG = n_itens / n_grupos
    print("Há", IporG, "itens por grupo se houver", n_grupos, "grupos.")

# Decidir quantos grupos se houver x itens/grupo
if answer == "g":
    pass