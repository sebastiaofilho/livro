class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mudarCor(self, cor2):
        self.cor = cor2

    def mostraCor(self):
        print(self.cor)


bola1 = Bola("azul", 5, "Couro")
bola1.mudarCor("cinza")
bola1.mostraCor()
