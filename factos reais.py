from math import log10, floor

def shorten(r):
    if r < 10**500:
        return r
    else:
        l = floor(log10(r))
        nr = r/(10**l)
        return str(nr)+"e"+str(l)

def fato(n):
    r = 1
    for i in range(n):
        r *= i+1
    return r

calc = int(input("Number: "))
print(shorten(fato(calc)))
input()
