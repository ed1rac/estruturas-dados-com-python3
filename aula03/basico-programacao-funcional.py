from functools import reduce

"""
Noções básicas de programação funcional em Python
Leitura complementar: http://nasemanadaprova.blogspot.com.br/2015/01/programacao-funcional-python.html

List Comprehension: http://www.python-course.eu/list_comprehension.php
Expressão lambda: http://blog.alienretro.com/entendendo-python-lambda/
Map, Filter and Reduce: http://book.pythontips.com/en/latest/map_filter.html

Map: aplicar uma função em todos os itens de uma ou mais sequências
Reduce: aplica uma função sobre uma sequencia e vai acumulando o valor de retorno da função a partir de um valor inicial (reduce foi removida do python3 (core) e está disponível no pacote functools, importado acima)
Filter: serve para filtrar/selecionar elementos de uma lista que correspondem a uma determinada condição
"""

# criar uma lista com os 100 primeiros números pares (100 inclusive) usando List Comprehension
pares = [n for n in range(101) if n % 2 == 0]
print(pares)

# expressão lambda para um função de potência
potencia = lambda x: x ** 2
print(potencia(2))

# função fatorial com lambda
fatorial = lambda n: n * fatorial(n - 1) if n > 1 else 1
print(fatorial(5))

# utilizando lambda com map (elevar a potência todos os itens da lista)
lista = [1, 2, 3, 44, 556, 78, 4, 67, 9, 2]
m = map(lambda x: x ** 2, lista)
for i in m: print(i, end=' ')

print()

# ou utilizando a função lambda "potencia" previamente definida
m2 = map(potencia, lista)
for i in m2: print(i, end=' ')

print()

# utilizando a função reduce para fazer o somatório da lista (1+2+3+44+556+78...)
print(reduce(lambda x, y: x + y, lista))

# neste exemplo, seria mais legível e fácil usar a função sum()
print(sum(lista))

print()

# usando filter para selecionar elementos de uma lista sob uma determinada condição

# selecionando na lista somente os números pares
filtro = filter(lambda x: x % 2 == 0, lista)
for i in filtro: print(i, end=' ')
