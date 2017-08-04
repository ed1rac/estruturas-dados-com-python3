"""
Leitura complementar: http://www.diveintopython3.net/unit-testing.html
"""

import unittest

# implementação

"""
função que recebe dois parâmetros, a e b e retorna a soma entre os dois.
"""
def soma(a, b):
    # função com implementada de forma errada
    return a + b * 2

def soma_corrigida(a, b):
    return a + b

# teste unitário do código
class TestBasico(unittest.TestCase):

    def test_soma_errada(self):
        # quer assegurar que 2+2 seja igual a 4, se quebrar o teste, a implemetação está errada
        self.assertEqual(4, soma(2, 2))
        # self.assertNotEqual(4, soma(2, 2)) validaria o teste, pois asseguraria que o teste iria falhar

    def test_soma_corrigida(self):
        self.assertEqual(4, soma_corrigida(2, 2))

    def test_dois_valores_iguais(self):
        self.assertTrue(3 > 2, 66 > 63)

unittest.main()
