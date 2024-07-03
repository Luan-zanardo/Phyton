'''Crie um programa que leia dois valores e mostre na tela um menu :
a. Somar
b. Multiplicar
c. Maior
d. Menor
e. Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''

def Soma(a,b):
    soma = a + b
    return soma

def Multiplicar(a,b):
    multiplicacao = a * b
    return multiplicacao

def Maior(a, b):
    if(a > b):
        maior = a
    else:
        maior = b
    return maior

def Menor(a, b):
    if(a < b):
        menor = a
    else:
        menor = b
    return menor

def menu():
    while True:
        a = int( input('Digite numero a: ') )
        b = int( input('Digite numero b: ') )
        opcao = int(input('1 - Somar\n' +
                          '2 - Multiplicar\n' +
                          '3 - Maior\n' +
                          '4 - Menor\n' +
                          '5 - Sair do programa\n'))
        if opcao==1:
            print(f'A soma de {a} e {b} é {Soma(a,b)}\n')
        elif opcao==2:
            print(f'A multiplicação de {a} e {b} é {Multiplicar(a,b)}\n')
        elif opcao==3:
            print(f'O maior numero é {Maior(a, b)}\n')
        elif opcao==4:
            print(f'O menor numero é {Menor(a, b)}\n')
        elif opcao==5:
            break
menu()