class Carro:
    def __init__(self, kmlitro):
        self.gasolina = 0
        self.kmlitro = kmlitro

    def andar(self, distancia):
        self.gasolina -= distancia / self.kmlitro

    def obtergasolina(self):
        print(self.gasolina)

    def adicionargasolina(self, litros):
        self.gasolina += litros

a = Carro(kmlitro=15)

a.adicionargasolina(20)
a.andar(100)
a.obtergasolina()