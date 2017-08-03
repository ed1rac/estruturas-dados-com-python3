"""
Material complementar: https://pythonhelp.wordpress.com/2013/01/10/desempacotamento-de-tupla/
"""

lista = [1, 2, 3, 4]

print('tipo: {0} | valor: {1}'.format(type(lista), lista))

# desempacotando a lista e atribuindo a variáveis
a, b, c, d = lista

print('tipo: {0} | a: {1}'.format(type(a), a))
print('tipo: {0} | b: {1}'.format(type(b), b))
print('tipo: {0} | c: {1}'.format(type(c), c))
print('tipo: {0} | d: {1}'.format(type(d), d))

# utilizando underscore _ para desempacotamento, ignorando o terceiro item da lista
x, y, _, z = lista

print('tipo: {0} | x: {1}'.format(type(x), x))
print('tipo: {0} | y: {1}'.format(type(y), y))
print('tipo: {0} | z: {1}'.format(type(z), z))

# desempacotando o primeiro e ultimo elemento
u, _, _, p = lista

print('tipo: {0} | u: {1}'.format(type(u), u))
print('tipo: {0} | p: {1}'.format(type(p), p))

# desempacotando strings
nome = "Robson"
primeira_letra, _, _, _, penultima_letra, ultima_letra = nome

print('tipo: {0} | nome: {1}'.format(type(nome), nome))
print('tipo: {0} | primeira letra: {1}'.format(type(primeira_letra), primeira_letra))
print('tipo: {0} | penultima letra: {1}'.format(type(penultima_letra), penultima_letra))
print('tipo: {0} | ultima letra: {1}'.format(type(ultima_letra), ultima_letra))

# desempacotando função com vários retornos
def funcao(x: int, y: int):
    return x ** 2, y ** 2

print(funcao(2, 4))
print(type(funcao(2, 4))) # <-- retorno multiplo de funções gera uma tupla no retorno com os valores contidos nesta.

# desempacotando o retorno da função em variaveis
retorno1, retorno2 = funcao(5, 6)
print(retorno1)
print(retorno2)
