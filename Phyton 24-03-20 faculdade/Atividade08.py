'''Desenvolva um programa que leia uma frase e um caractere. Em seguida, exiba ambos e o número de ocorrências do caractere na frase.​'''

frase = input("Digite um frase: ").lower()
caracter = input("Digite um caracter: ").lower()
contagem = frase.count(caracter)

print("O numero do caracter {} nesse frase é igual a {}".format(caracter, contagem))