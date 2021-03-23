class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        print(idade)
        return cls(nome, idade)


x = Pessoa
x.ano_nascimento('Tiao', 1984)
x.ano_nascimento('Livia', 1986)
x.ano_nascimento('Luis', 1981)

from random import randint
class Prudente:
    @staticmethod
    def gerador_id():
        gerador = randint(100, 999)
        return gerador


print(Prudente.gerador_id())