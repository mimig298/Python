from math import log10, floor

def shorten(r):
    if r < 10**500:
        return r
    else:
        l = floor(log10(r))
        nr = r/(10**l)
        return str(nr)+"e"+str(l)

def fato(n, e=1):
    r = n
    while n - e > 1:
        n -= e
        r *= n
    return r

def som(n, i=1, e=1):
    r = i
    while i < n:
        i += e
        r += i
    return r
