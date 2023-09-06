valorA= int(input("Digite o valor de a: "))
valorB= int(input("Digite o valor de b: "))
valorC= int(input("Digite o valor de c: "))

soma = (valorA + valorB)
# somando os valores e verificando se a soma é menor que o "c"

if soma < valorC:
    print(" A soma de a+b é menor que c!")

if soma > valorC:
    print("A soma de a+b é maior que c!")