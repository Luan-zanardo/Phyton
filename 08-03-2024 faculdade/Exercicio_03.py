import math

raio = int(input("Raio: "))

perimetro = 2 * math.pi * raio
area = math.pi * (raio**2)

print(f"Perimetro: {perimetro:.2f}")
print(f"Área: {area:.2f}")