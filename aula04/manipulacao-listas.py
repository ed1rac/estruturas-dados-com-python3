"""
Material complementar: http://www.python-course.eu/python3_list_manipulation.php
"""

nomes = ['robson', 'maria', 'joao', 'silva']
numeros = [3, 4, 6, 8]

# concatenando listas
print(nomes + numeros)

# removendo itens da lista (por índice)
nomes.pop(0) # <-- remove o primeiro item da lista
print(nomes)

nomes.pop(len(nomes) - 1) # <-- remove o último item da lista
print(nomes)

# removendo itens da lista pelo elemento que se deseja remover (via função remove)
numeros.remove(4)
print(numeros)

"""
Removendo um item inexsitente gera exceção:

nomes.remove('robson')
print(nomes)
ValueError: list.remove(x): x not in list
"""

# iterando os elementos da lista
for item in nomes:
    print(item)

# convertendo uma lista para uma tupla
tupla_nomes = tuple(nomes)
print(tupla_nomes)

# adicionando elementos em uma lista
nomes.append('carla')
nomes.append('pedro')
numeros.append(456)
numeros.append(0)

print(nomes)
print(numeros)

# adicionando elemento em uma posição da lista
nomes.insert(0, 'roberto') # <-- adiciona no início (índice 0)
nomes.insert(2, 'adriana') # <-- adiciona na terceira posição
print(nomes)

# ordenando uma lista (crescente)
numeros.sort()
print(numeros)

# manipular elementos com slice
print(nomes[-1]) # <-- exibe o último elemento
print(nomes[-2]) # <-- exibe o penultimo elemento
print(nomes[1:4]) # <-- exibe do segundo até o quarto elemento (não inclue o quarto)
print(nomes[2:]) # <-- exibe do terceiro item até o final
print(numeros[::-1]) # <-- inverte a lista
