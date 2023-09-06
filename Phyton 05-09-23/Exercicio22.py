'''Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
Desconsiderando o valor 1000 da parada.'''

soma = 0
numeros = 0

def menu():

    global soma 
    global numeros

    while True:
        a = int(input("Digite um numero: "))

        if(a == 1000):
            print(f"Foram digitados {numeros} numeros")
            print(f"A soma final desconsiderando o valor 1000 é {soma}")
            break
        else:
            soma += a
            numeros += 1
menu()