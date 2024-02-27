import unittest
from math import sqrt, exp, sin, e
from biseccion import biseccion
from newton import newton_raphson
from Integracion import suma_riemann
def f(x):
    return sqrt(x+1)

class TestBiseccion(unittest.TestCase):
    def test_biseccion_exp(self):
        f = lambda x: exp(x) - 3 * x ** 2
        a, b = 0, 1
        tol = 0.02
        ni = 100
        self.assertIsNone(biseccion(f, a, b, tol, ni))

    def test_biseccion_sin_exp(self):
        f = lambda x: sin(x) - e ** -x
        a, b = 0, 1
        tol = 0.02
        ni = 100
        self.assertIsNone(biseccion(f, a, b, tol, ni))

class TestNewtonRaphson(unittest.TestCase):
    def test_newton_raphson_exp(self):
        f = lambda x: exp(x) - 3 * x ** 2
        df = lambda x: exp(x) - 6 * x
        x0 = 0.7
        tol = 0.02
        self.assertAlmostEqual(newton_raphson(f, df, x0, tol), 0.9100079800667897)

    def test_newton_raphson_quadratic(self):
        f = lambda x: x ** 2 + 2 * x - 8
        df = lambda x: 2 * x + 2
        x0 = 0.7
        tol = 0.02
        self.assertAlmostEqual(newton_raphson(f, df, x0, tol), 2.00020555596486)

class test_integracion_numerica(unittest.TestCase):
    def test_suma_riemann(self):
        a = -1      # inicio del intervalo
        b = 1     # fin del intervalo
        n = 5   # numero de participaciones
        self.assertEqual(suma_riemann(f,a, b, n),1.5548955608445105)

if __name__ == "__main__":
    unittest.main()
