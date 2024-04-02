import random

vetor = [0]*10
pares = 0
impares = 0

#adicionar numeros aleatorios de 1 a 10
for cont in range (10):
    vetor[cont] = random.randint(1,50)
    if ((vetor[cont] %2) == 0):
        pares = pares + 1
    else:
        impares = impares + 1

#mostrar dados do vetor
for cont in range(10):
    print(vetor[cont])

print("Total de números pares: ",pares)
print("Total de números impares ",impares)