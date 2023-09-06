#importando a biblioteca random
import random

#criar variaveis
vetor = [0]*10
menor = 200
maior = 0


#contador
for cont in range (10):
    vetor[cont] = random.randint(10,100)
    if (vetor[cont] > maior):
        maior = vetor[cont]
    if (vetor[cont] < menor):
        menor = vetor[cont]

for cont in range(10):
    print(vetor[cont])

print ('Maior valor: ',maior)
print ('Menor valor: ',menor)