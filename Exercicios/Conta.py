class Conta:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


conta1 = Conta(111, "Tião")
print(conta1.nome)
conta1.alterarNome("Luis")
print(conta1.nome)
conta1.depositar(1000)
print(conta1.saldo)
conta1.sacar(300)
print(conta1.saldo)



