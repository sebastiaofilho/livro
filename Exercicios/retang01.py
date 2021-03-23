from Retang3 import Retangulo

# Entrada de dados:
largura = float(input("Digite valor da largura em metros: "))*100
comprimento = (float(input("Digite o valor do comprimento em metros: ")))*100

# Primeiramanete calcularemos a área de cada cerâmica
calc = Retangulo(20, 20)
area1 = calc.area()

# Agora será calculada a área do ambiente.
calc = Retangulo(largura, comprimento)
area2 = calc.area()

# Aqui calcular-se-á o perímetro:
perimetro = calc.perimetro()

# Cálculo da quantidade de cerâmica requerida com acréscimo de 10%:
print(f" Serão necessárias {area2/area1} cerâmicas")
print(f" Serão necessários {(perimetro)/100}m de rodapés")
