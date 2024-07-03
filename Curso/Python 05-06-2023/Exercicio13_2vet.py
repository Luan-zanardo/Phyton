list_values = []
repeat = []

for i in range (10):
    valor = int(input("Qual valor: "))
    if valor in list_values:
        repeat.append(valor)
    list_values.append(valor)

print("Valores do vetor: ")
print(list_values)
print("Valores repetidos no vetor: ")
print(repeat)

