peso = int(input("Digite peso (kg): "))
altura = int(input("Digite altura (metros): "))

imc = peso / (altura**2)
print(f"IMC: {imc}")