'''15) Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, 
deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero 
e imprimir o resultado da divisão do primeiro valor lido pelo segundo valor lido. FOR'''

valor1 = int(input("Digite valor 1: "))
valor2 = int(input("Digite valor 2: "))
while True:
    if(valor2 == 0):
        valor2 = int(input("Digite valor 2: "))
    else:
        break

divisao = valor1 / valor2

print(f"{valor1} / {valor2}: {divisao}")