#importando a biblioteca random
import random

#criar variaveis
vetor = [0]*10
menor = 200
maior = 0
posicaomaior = 0


#contador
for cont in range (10):
    vetor[cont] = random.randint(10,100)
    if (vetor[cont] > maior):
        maior = vetor[cont]     
        posicaomaior = cont     #Seta a posicao em queo contador está

for cont in range(10):
    print(vetor[cont])

print ('Maior vetor : ',maior," posiçaõ do vetor: ",posicaomaior)
