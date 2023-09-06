vetor = [0]*5

print("Digite 5 valores abaixo: ")

for cont in range (5):
    vetor[cont] = int(input("Digite um valor: "))
    if (vetor[cont] == vetor[cont-1]):
        print("Valor repetido",vetor[cont])

print(vetor)