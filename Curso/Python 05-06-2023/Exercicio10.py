#quantidade de notas a ser cadastradas
nmrnotas = int(input('Quantas notas deseja calcular? '))
#vetor
notas = []
#contaor para obter todas notas
for cont in range (nmrnotas):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

#calcular a media e printar na tela 
media = sum(notas)/nmrnotas             #funcao 'sum' somas todos valores da lista 'notas' 
print("Média das notas: ",media)