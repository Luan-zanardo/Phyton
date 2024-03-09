import math

raio1 = int(input("Raio 1: "))
raio2 = int(input("Raio 2: "))

area = (math.pi * (raio1**2)) - (math.pi * (raio2**2))

print(f"Área da coroa: {area:.2f}")