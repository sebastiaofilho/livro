class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print('Chamando a mensagem de prova.')
        return self.__nome.title()
