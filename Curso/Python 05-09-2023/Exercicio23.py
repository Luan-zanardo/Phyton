'''Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
não continuar a escrever valores.'''

soma = 0
numeros = 0
maior = 0
menor = 9999999999

def menu():

    global soma
    global numeros
    global maior
    global menor
    
    while True:
        a = int(input("Digite um numero: "))
        soma += a
        numeros += 1

        if(a > maior):
            maior = a
        if(a < menor):
            menor = a 
        op = input("Você deseja continuar escrever os valores ?\n Digite (S) para sim e (N) para não: ")

        if(op == "N"):
            print(f"A média de todos os valores lidos é {soma / numeros}")
            print(f"O maior numero é {maior}")
            print(f"O menor numero é {menor}")
            break
menu()