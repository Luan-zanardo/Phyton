""" 13) Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles. """

lista = []
soma = 0

for i in range(5):
    valor = int(input("Digite um valor: "))
    lista.append(valor)

for i in range(len(lista)):
    soma += lista[i]

print(f"a soma de todos os numeros da lista é {soma}")