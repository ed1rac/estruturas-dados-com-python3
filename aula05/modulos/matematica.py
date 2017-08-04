"""
Criação de módulos com python.
https://docs.python.org/3.6/tutorial/modules.html
"""

def fatorial(n: int) -> int:
    if (n == 0):
        return 1
    return n * fatorial(n - 1)

def potencia(base: float, exp: float) -> float:
    if (exp == 0):
        return 1
    return base * potencia(base, exp - 1)

def area_quadrado(lado: float) -> float:
    return lado * lado
