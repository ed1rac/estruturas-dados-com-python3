"""
Números pseudo-aleatórios não devem ser utilizados para criptografia ou propositos de segurança.
A biblioteca secrets deve ser utilizada nos casos de segurança e criptografia.

https://docs.python.org/3/library/random.html
https://docs.python.org/3/library/secrets.html#module-secrets
"""

import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# retorna um numero inteiro entre 0 e 50
print(random.randrange(50))

# retorna um número inteiro entre 40 e 99 (inclusive)
print(random.randint(40, 99))

# seleciona/sorteia um elemento da lista
print(random.choice(lista))

# embaralhar uma lista
random.shuffle(lista)
print(lista)
random.shuffle(lista)
print(lista)

# recuperar n elementos de uma lista aleatoriamente
print(random.sample(lista, 3))
print(random.sample(lista, 5))

# gerando numero de ponto flutuante (entre 0 e 1)
print(random.random())

# gerando numeros de ponto flutuante entre 3 e 55
print(random.uniform(3, 55))
