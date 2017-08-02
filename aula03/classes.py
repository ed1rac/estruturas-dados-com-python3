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
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, nome: str) -> str:
        if (len(nome) > 3):
            self.__nome = nome
        else:
            raise ValueError("Nome precisa ter ao menos 3 caracteres")

    def idade(self, idade: int) -> int:
        if (idade > 0):
            self.__idade = idade
        else:
            raise ValueError("Idade deve ser maior que zero")

p = Pessoa('R2', 23)
print(p.nome)
