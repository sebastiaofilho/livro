class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarValores(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura

    def area(self):
        area = self.base * self.altura
        return area

    def perimetro(self):
        perimetro = (2 * self.base) + (2 * self.altura)
        return perimetro


