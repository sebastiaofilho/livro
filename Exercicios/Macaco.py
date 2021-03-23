class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = []


macaco1 = Macaco('Chico', 0)
macaco2 = Macaco('Inacio', 0)
macaco2.comer("Banana")
macaco2.comer("Maçã")
macaco2.comer("Coco")
estomago = macaco2.verBucho()
print(estomago)

