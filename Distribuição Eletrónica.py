limites = []
lim = 118

for n in range(10):
    limites.append(2*(n+1)**2)

els = []
for x in range(lim):
    elecs = x+1
    distr = [0]*100
    n = 1
    while elecs > 0:
        if distr[n-1] >= limites[n-1]:
            n += 1
        distr[n-1] += 1
        elecs -= 1
    while 0 in distr:
        distr.remove(0)
    if x == 18:
        els.append([2, 8, 8, 1])
    elif x == 19:
        els.append([2, 8, 8, 2])
    else:
        els.append(distr)
    if x%(lim/10) == 0:
        print(x)

for elecs in range(len(els)):
    distr = els[elecs]
    elecs += 1
    period = len(distr)
    group = int(str(distr[period-1])[::-1][0])
    if group >= 3:
        group += 10
    nd = ""
    for lay in distr:
        nd = nd + str(lay) + ":"
    nd = nd[:len(nd)-1]
    print(f"N.Atómico: {elecs}, Distribuição: {nd}, Localização: {group},{period}")
