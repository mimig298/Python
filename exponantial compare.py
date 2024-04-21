x = 0
calc = 100
start = 10
scale = 1.15

func = []
def f(x):
    return round(start*(scale**(x-1)))
for x in range(calc):
    func.append(f(x))

recu = [-1]*calc
def recursive(x, mem):
    if x == 0:
        mem[x] = f(x)
    elif x == 1:
        mem[x] = start
    else:
        mem[x] = round((mem[x-1])*scale)
    return mem
for x in range(calc):
    recu = recursive(x, recu)

for x in range(len(func)):
    print(func[x], recu[x])
    #print(round(func[x]/recu[x], 2))