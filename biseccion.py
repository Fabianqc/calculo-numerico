from math import *

def biseccion(f, a, b, tol, ni):
    # Variables
    Error_a = 100  # Error aproximado relativo.
    p_actual = a   # Punto medio actual
    p_anterior = b  # Punto medio previo
    contador = 1   # Contador de número de iteraciones

    print("\nMétodo de Bisección\n")  # Título

    while contador < ni and Error_a > tol:
        p_anterior = p_actual
        p_actual = (a + b) / 2

        if f(a) * f(p_actual) < 0:  # Cambia de signo en el intervalo [a,m]
            b = p_actual
        if f(p_actual) * f(b) < 0:  # Cambia de signo en el intervalo [m,b]
            a = p_actual

        Error_a = abs((p_actual - p_anterior) / p_actual)
        print('Iteración', contador, 'intervalo: [', a, ',', b, ']')
        contador = contador + 1

    print('\nLa mejor solución aproximada se encuentra en m(', contador - 1, ') =', p_actual, '\n')
    print("El error relativo es: ", Error_a)

if __name__ == '__main__':
    f = lambda x: sin(x) - e**-x  # Definición de la función
    a = 0  # Intervalo a
    b = 1  # Intervalo B
    tol = 0.03  # Tolerancia
    ni = 50  # Número de iteraciones
    solucion = biseccion(f, a, b, tol, ni)
