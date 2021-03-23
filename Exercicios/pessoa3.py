class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade <= 21:
            self.crescer(0.5)

    def engordar(self, eng=1.0):
        self.peso += eng

    def emagrecer(self, ema=1.0):
        self.peso -= ema

    def crescer(self, tam=1.0):
        self.altura += tam


pess = Pessoa("Luis",19.0, 70.0, 170.0)
pess.engordar(5.0)
pess.crescer(5.0)
pess.emagrecer(2.0)
print(pess.altura)
pess.envelhecer()
print(pess.altura)

