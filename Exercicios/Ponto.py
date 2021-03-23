class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self, x, y):
        print(f"{x}, {y}")


class Retangulo:
    from Ponto import Ponto

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        centroA = self.altura/2
        centroB = self.largura/2
        teste.imprimir(centroA, centroB)

    def area(self):
        area = self.altura*self.largura
        print(f'A área do retângulo é {area}.')


teste = Retangulo(10, 2)
teste.encontrarCentro()
