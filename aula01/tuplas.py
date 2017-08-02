"""
Tuplas são listas de valores imutáveis
Usa-se () para criar uma tupla
Artigo complementar: http://www3.ifrn.edu.br/~jurandy/fdp/doc/aprenda-python/capitulo_09.html
"""

# tuplas (imutável)
tupla = ('robson', 123, 3.456, 'python')
print(tupla)
print(type(tupla))
print(tupla[1])

"""
se tentar:
tupla(0) = 'Robson_modificado'
print(tupla)
Vai gerar exceção do tipo TypeError:
 TypeError: 'tuple' object does not support item assignment
"""

# igualmente às tuplas, string é imutável
nome = 'Robson'
print(nome)

# strings podem ter seus caracteres acessados como uma lista
print(nome[0])
print(nome[1])

# mas não é possível modificar
"""
se tentar:
nome[1] = 'Z'
print(nome)
vai gerar:
 TypeError: 'str' object does not support item assignment
"""
