class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarValores(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura
        return self.base, self.altura

    def area(self, lado1, lado2):
        area = lado1 * lado2
        return area

    def perimetro(self, base, altura):
        perimetro = (2 * base) + (2 * altura)
        return perimetro


# Entrada de dados:
largura = int(input("Digite valor da largura: "))
comprimento = int(input("Digite o valor do comprimento: "))

# Primeiramanete calcularemos a área de cada cerâmica
calc = Retangulo(20, 10)
area1 = calc.area(20, 10)

# Agora será calculada a área do espaço
area2 = calc.area(largura, comprimento)

# Aqui calcular-se-á o perímetro:
perimetro = calc.perimetro(largura, comprimento)

# Neste bloco será calculada a área total do rodapé
arearodape = calc.area(perimetro, 5)

# Cálculo da quantidade de cerâmica requerida com acréscimo de 10%:
superficie = area2/area1
rodape = arearodape/area1
print(f"Serão necessárias {round((superficie + rodape)*1.1)} cerâmicas")
