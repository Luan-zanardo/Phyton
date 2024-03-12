class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    def calcularPerimetro(self):
        valor = self.ladoA + self.ladoB + self.ladoC
        print(valor)
    def getMaiorLado(self):
        valor = 0
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            valor = self.ladoA
            print(valor)
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            valor = self.ladoB
            print(valor)
        else:
            valor = self.ladoC
            print(valor)
    def area(self):
        print((self.ladoB * 5) / 2)

triangulo1 = Triangulo(2, 22, 176)
triangulo1.calcularPerimetro()
triangulo1.getMaiorLado()