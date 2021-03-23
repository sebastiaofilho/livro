class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarValores(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura
        return self.base, self.altura

    def area(self):
        area = self.base * self.altura
        return area

    def perimetro(self, base, altura):
        perimetro = (2 * base) + (2 * altura)
        return perimetro


# Primeiramanete calcularemos a área de cada cerâmica
calc = Retangulo(20, 10)
area1 = calc.area()

# Agora será calculada a área do espaço
calc.mudarValores(280, 100)
area2 = calc.area()

# Aqui calcular-se-á o perímetro:
perimetro = calc.perimetro(280, 100)

# Neste bloco será calculada a área total do rodapé
calc.mudarValores(perimetro,5)
arearodape = calc.area()

# Cálculo da quantidade de cerâmica requerida:
superficie = area2/area1
rodape = arearodape/area1
print(f"Serão necessárias {round((superficie + rodape)*1.1)} cerâmicas")
