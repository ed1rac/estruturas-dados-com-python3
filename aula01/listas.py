"""
Listas são como os vetores em php ou javascript
Usa-se [] para criar uma lista
Artigo complementar para manipulação de listas: http://www.devfuria.com.br/python/listas/
"""

lista_numeros = [1, 2, 3, 4, 54]
lista_string = ['abc', 'sdf', 'tre', '456']
lista_mista  = [1, 'robson', 3, 4, 'python', 3.54576]

print(type(lista_numeros))
print(lista_numeros)
print(lista_string)
print(lista_mista)

# modificando elementos pelo indice
lista_mista[4] = 'Python3'
print(lista_mista)
