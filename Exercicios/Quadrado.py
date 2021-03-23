class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novoLado):
        self.lado = novoLado

    def retornarValor(self):
        return self.lado

    def calcularArea(self):
        area = self.lado * self.lado
        return area


quadrado = Quadrado(5)
quadrado.mudarLado(10.1)
area = quadrado.calcularArea()
lado = quadrado.retornarValor()
print(lado)
print(area)