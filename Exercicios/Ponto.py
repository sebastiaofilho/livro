class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimirPonto(self):
        print(f"{self.x}, {self.y}")


class Retangulo:

    def __init__(self, largura, altura, x, y):
        self.largura = largura
        self.altura = altura
        self.vertice = Ponto(x, y)

    def encontrarCentro(self):
        centroA = self.altura/2
        centroB = self.largura/2
        teste.imprimir(centroA, centroB)

    def area(self):
        area = self.altura*self.largura
        print(f'A área do retângulo é {area}.')

    def imprimirRetangulo(self):
        print(f'{self.altura} e {self.largura} e {self.vertice.imprimirPonto()}')

#

#teste = Retangulo(10, 2)
#teste.encontrarCentro()
