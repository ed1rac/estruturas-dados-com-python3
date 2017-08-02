"""
Dicionários são um tipo específico como um map no java, ou um json do javascript.
É característico por chave:valor.
Usa-se {} para criar um dicionário
Artigo complementar: https://panda.ime.usp.br/pensepy/static/pensepy/11-Dicionarios/dicionarios.html
"""

dicionario = {'robson': 30, 'joao': 54, 'maria': 20}
print(type(dicionario))
print(dicionario['joao'])

# dicionario complexos (com dicionários, listas e tuplas)

d = {
    'robson': {
        'idade': 30,
        'altura': 176,
        'preferencias': ['abc', 123],
        'localizacao': (-34.676554, 12.456322)
    },
    'joao': {
        'idade': 54,
        'altura': 165
    },
    'maria': {
        'idade': 20,
        'altura': 169
    }
}

print(d)
print(d['robson'])
print(d['robson']['idade'])
print(d['robson']['altura'])
print(d['robson']['localizacao'])
print(type(d['robson']['preferencias']))
print(type(d['robson']['localizacao']))

# percorrendo pelas chaves de um dicionário
for chave in d:
    print(chave)
