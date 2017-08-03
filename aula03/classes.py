"""
Python pode ser utilizado de forma procedural, funcioal e orientado a objetos
Documentação: https://docs.python.org/3/tutorial/classes.html
"""

class Pessoa:
    def __init__(self, nome: str, idade: int):
        # atributos private (__)
        self.__nome = nome
        self.__idade = idade

        # "setando" os valores através dos respectivos setters (aproveitando a validação)
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def idade(self) -> int:
        return self.__idade

    @nome.setter
    def nome(self, nome: str):
        if (len(nome) > 3):
            self.__nome = nome
        else:
            raise ValueError("Nome precisa ter ao menos 3 caracteres")

    @idade.setter
    def idade(self, idade: int):
        if (idade > 0):
            self.__idade = idade
        else:
            raise ValueError("Idade deve ser maior que zero")

"""
Python ignora o type hint, a utilidade não é forçar a linguagem a ser fortemente tipada, veja mais em: https://www.python.org/dev/peps/pep-0484/
p = Pessoa('Rnsd', '23')
print(p.idade)
TypeError: '>' not supported between instances of 'str' and 'int'
"""

"""
p = Pessoa('Rn', 23)
print(p.idade)
ValueError: Nome precisa ter ao menos 3 caracteres
"""

"""
p = Pessoa('Robson', -10)
print(p.idade)
ValueError: Idade deve ser maior que zero
"""

# p.nome e p.idade não está acessando o atributo diretamente, pois são private (__). Estão sendo recuperados via @property
p = Pessoa('Robson', 30)
print('{0} esta com {1} anos de idade'.format(p.nome, p.idade))

# utilizando o setter da property idade
p.idade = 32
print('{0} esta com {1} anos de idade'.format(p.nome, p.idade))
