class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def getverBucho(self):
        return self.bucho

    def setdigerir(self):
        self.bucho = []

"""
macaco1 = Macaco('Chico', 0)
macaco2 = Macaco('Inacio', 0)
macaco2.comer("Banana")
estomago = macaco2.getverBucho()
print(estomago)
macaco2.comer("Maçã")
estomago = macaco2.getverBucho()
print(estomago)
macaco2.comer(macaco1)
estomago = macaco2.getverBucho()
print(estomago)
macaco2.setdigerir()
estomago = macaco2.getverBucho()
print(estomago)
"""


