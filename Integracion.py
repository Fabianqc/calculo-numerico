from math import *

def f(x):
    return sqrt(x + 1)

def midpoint_rule(f, a, b, n):
    h = (b - a) / n
    result = 0

    for i in range(n):
        midpoint = a + (i + 0.5) * h
        result += h * f(midpoint)

    return result

if __name__ == '__main__':
    a = -1      # inicio del intervalo
    b = 1       # fin del intervalo
    n = 5       # numero de participaciones

    midpoint_result = midpoint_rule(f, a, b, n)

    print("\t.:Integracion Numerica:.")
    print("-------------------------------------")
    print("Regla del Punto Medio en función f(x) para", a, "y", b, "con", n, "subintervalos:", midpoint_result)
    print("-------------------------------------")
