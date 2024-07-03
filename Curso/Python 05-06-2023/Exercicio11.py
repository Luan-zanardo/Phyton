vetor = []

negativo = 0
positivo = 0

for cont in range (10):
    valor = float(input("Digite qualquer valor, positivo ou negativo: "))
    if valor < 0:
        negativo += 1
    if valor > 0:
        positivo = positivo + valor
    vetor.append(valor)

print("Quantidade de numeros negativos digitados: ",negativo)
print("Soma de todos valores positivos digitados: ",positivo)