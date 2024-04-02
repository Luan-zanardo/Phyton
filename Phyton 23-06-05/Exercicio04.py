import random

vetor = [0]*6

for cont in range (6):
    vetor[cont] = random.randint(1,50)

print("Valores sortidos: ")
for cont in range(6):
    print(vetor[cont])
