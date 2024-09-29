# Etapas numa fábrica
# Têm dependências
# Isto ficaria bueda bom em C
# oh well

e_tempo = [5, 10, 15, 5, 5, 8, 5, 5]
tempo = 0
local_e_tempo = []

def subtract(index):
    if local_e_tempo[index] > 0:
        local_e_tempo[index] -= 1

while sum(e_tempo) > 0:
    local_e_tempo = e_tempo.copy()
    subtract(0)
    if e_tempo[0] == 0:
        subtract(1)
        subtract(2)
        subtract(3)
    if e_tempo[1] + e_tempo[2] == 0:
        subtract(4)
    if e_tempo[2] + e_tempo[3] == 0:
        subtract(5)
    if e_tempo[4] == 0:
        subtract(6)
    if e_tempo[5] + e_tempo[6] == 0:
        subtract(7)
    e_tempo = local_e_tempo.copy()
    tempo += 1
    print(e_tempo, tempo)
