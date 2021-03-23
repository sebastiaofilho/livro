class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual/100))

    #getter
    @property
    def preco(self):
        print('salvando')
        return self.preco_valido

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))
        self.preco_valido = valor


produto1 = Produto('Mala', 250)
produto2 = Produto('Oculos', 'R$ 145')
produto3 = Produto('Sunga', 15)
produto4 = Produto('Biquini', 25)
produto5 = Produto('Chapéu', 29)
print(produto5.preco)
print(produto1.nome)
produto2.desconto(50)
print(produto2.preco)