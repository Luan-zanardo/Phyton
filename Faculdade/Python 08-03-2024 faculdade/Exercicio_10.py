import math

diametro = float(input("Diametro em metros: "))
velocidade = float(input("Velocidade m/s: "))

taxafluxo = math.pi* (diametro**2) / 4 * diametro

print(f"Taxa de fluxo volumétrico: {taxafluxo:.2f} m³/s")