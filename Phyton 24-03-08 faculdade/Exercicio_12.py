import math

raio = float(input("Raio: "))

apotema = raio * math.sqrt(3) / 2
lateral = 2 * raio
areaTriangulo = 0.5 * lateral * apotema
areaHexagono = 6 * areaTriangulo

print(f"A área do hexagono é: {areaHexagono:.2f}")