from math import sin, exp, e

def bisection_method(func, interval, tolerance, max_iterations):
    a, b = interval
    p_current = a
    p_previous = b
    error = 100
    iteration = 1

    print("\nBisection Method\n")

    while iteration < max_iterations and error > tolerance:
        p_previous = p_current
        p_current = (a + b) / 2

        if func(a) * func(p_current) < 0:
            b = p_current
        elif func(p_current) * func(b) < 0:
           
