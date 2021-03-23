class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self, numero):
        print(f'Titular: {self.__titular}\nConta: {numero}\nSaldo: R$ {self.__saldo}\nLimite: R$ {self.__limite}')
        print(f'Disponível para saque: R$ {self.__saldo + self.__limite}')

    def sacar(self, saque):
        if self.__saldo + self.__limite > saque:
            self.__saldo -= saque
        print(self.__saldo)

    def depositar(self, deposito):
        self.__saldo += deposito
        print(self.__saldo)

    def transferir(self, valor, conta2):
        self.sacar(valor)
        conta2.depositar(valor)

    def get__limite(self):
        print('Mensagem de teste.')
        return self.__limite

    def set__limite(self, limite):
        """

        :param limite: o valor do novo limite
        :return: none

        Tudo bem para um exemplo, mas a lógica tem erro, pois, imagine
        que o cliente  tenha um  limite de R$ 2000,00, do qual já está
        usando R$ 1567,92.
        Agora ele quer aumentar o limite para R$ 3000,00.  Na hora que
        o bancário setar o novo limite em R$ 3.000,00, isso vai apagar
        gar os R$ 1567,92 que o cliente já estava usando.

        """
        self.__limite = limite
        print(self.__limite)


