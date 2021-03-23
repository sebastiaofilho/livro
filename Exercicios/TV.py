class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self, canal):
        if 0 < canal <= 99:
            self.canal = canal
        else:
            print("Canal desejado é inválido")

    def aumentarVolume(self, volume=1):
        if self.volume + volume <= 30:
            self.volume += volume
        else:
            self.volume = 30
            print("O volume não pode mais ser aumentado.")

    def abaixarVolume(self, volume=1):
        if self.volume - volume > 0:
            self.volume -= volume
        else:
            self.volume = 0
            print("Mudo")


televisao = Tv(43, 20)
print(televisao.canal)
televisao.mudarCanal(12)
print(televisao.canal)
print(televisao.volume)
televisao.aumentarVolume(8)
televisao.abaixarVolume(-30)
print(televisao.volume)