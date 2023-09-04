'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato'''

candidato1 = 0
candidato2 = 0
candidato3 = 0

a = int(input("Digite a quantidade de eleitores: "))

for i in range(a):
    opcao = int(input('1 - Candidato 1\n' +
                        '2 - Candidato 2\n' +
                        '3 - Candidato 3\n'))
    if opcao==1:
        candidato1 += 1
    elif opcao==2:
        candidato2 += 1
    elif opcao==3:
        candidato3 += 1

print("Quantidade de votos: ")
print(f"Candidato 1: {candidato1} votos")
print(f"Candidato 2: {candidato2} votos")
print(f"Candidato 3: {candidato3} votos")