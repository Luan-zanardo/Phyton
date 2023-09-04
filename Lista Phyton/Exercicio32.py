'''32) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
obtidos os seguintes dados:
a. Código da cidade; (digitado pelo usuário)
b. Número de veículos de passeio (em 1999); (digitado pelo usuário)
c. Número de acidentes de trânsito com vítimas (em 1999). (digitado pelo usuário)
Deseja-se saber:
b. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
c. Qual a média de veículos nas cinco cidades juntas;
d. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio'''

maior = 0
menor = 99999999
totalVeiculos = 0
totalCidades = 0
mediatotal = []
totalVeiculoslista = []
listaIndices = []

for i in range(5):
    codigoCidade = int(input("Digite o código da cidade: "))
    veiculos = int(input("Digite quantos veiculos de passeio: "))
    acidentes = int(input("Digite o numero de acidentes de trânsito: "))

    indice = veiculos/acidentes
    listaIndices.append(indice)
    totalVeiculoslista.append(veiculos)

    if(indice < menor):
        menor = indice
        menorcidade = codigoCidade
    elif(indice > maior):
        maior = indice
        maiorcidade = codigoCidade

    if veiculos < 2000:
        mediatotal.append(acidentes)

mediaVeiculos = sum(totalVeiculoslista) / len(totalVeiculoslista)
print(f"O maior índice de acidentes é da cidade {maiorcidade} sendo {round(maior, 2)}")
print(f"O menor índice de acidentes é da cidade {menorcidade} sendo {round(menor, 2)}")
print(f"A média de veículos nas cinco cidades juntas é: {round(mediaVeiculos, 2)}")

if (len(mediatotal) > 0):
    mediaAcidentes = sum(mediatotal)/len(mediatotal)
    print(f"A média de acidentes de trânsito nas cidades com menos de 2000 veículos é {round(mediaAcidentes, 2)}")