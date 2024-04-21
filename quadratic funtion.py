from math import sqrt

def quad(a, b, c):
    disc = b**2 - 4*a*c
    if disc < 0:
        return []
    else:
        return [(-b-sqrt(disc))/(2*a), (-b+sqrt(disc))/(2*a)]
