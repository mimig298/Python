a = 1
b = 2.3
c = 0.5
d = 20

tests = 100
step = 1
results = []
for num in range(tests):
    x = num*step
    results.append(round(a*x**3 + b*x**2 + c*x + d, 3))
    
for result in range(len(results)):
    sResult = result * step
    print(" "*(len(str(tests))-len(str(sResult))) + "f("+str(sResult)+") = " + str(results[result]))