from math import *

def f(x):
    return exp(x) - 3 * x ** 2

def df(x):
    return exp(x) - 6 * x

def newton_raphson(f, df, x0, tol, max_iter=5):
    i = 0
    Error_a = 100
    print("\nMétodo de Newton-Raphson\n")
    print("| i | xi | xi+1 |")
    print("----------------------")

    while i < max_iter and Error_a > tol:
        x1 = x0 - f(x0) / df(x0)
        print('|', i, '|', x0, '|', '|', x1, '|')
        
        if abs(x1 - x0) < tol * abs(x1):
            return x1
        
        x0 = x1
        i += 1

    print('\nLa mejor solución aproximada se encuentra en m(', i - 1, ') =', x1, '\n')    
    raise ValueError("El método de Newton-Raphson no converge después de %d iteraciones." % max_iter)

if __name__ == '__main__':
    x0 = 0.7  # Initial guess for x
    tol = 0.02  # Tolerance
    root = newton_raphson(f, df, x0, tol)  # Finding the root of f
    print('\nfin')
