'''Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida. 
Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
a. Soma de 2 números.
b. Diferença entre 2 números (maior pelo menor).
c.Produto entre 2 números.
d. Divisão entre 2 números (o denominador não pode ser zero).'''

def Soma(a,b):
    soma = a + b
    return soma

def Difereca(a,b):
    if(a > b):
        diferenca = a - b
    elif(b > a):
        diferenca = b - a
    else:
        diferenca = a - b
    return diferenca

def Produto(a,b):
    produto = a * b
    return produto

def Divisao(a, b):
    divisao = a / b
    return divisao

def menu():
    while True:
        opcao = int(input('1 - Soma de 2 números\n' +
                          '2 - Diferença entre 2 números\n' +
                          '3 - Produto entre 2 números\n' +
                          '4 - Divisão entre 2 números\n' +
                          '5 - Sair\n'))
        if opcao==1:
            a = int( input('Digite numero a: ') )
            b = int( input('Digite numero b: ') )
            print(f'A soma de {a} e {b} é {Soma(a,b)}\n')
        elif opcao==2:
            a = int( input('Digite numero a: ') )
            b = int( input('Digite numero b: ') )
            print(f'A diferença de {a} e {b} é {Difereca(a,b)}\n')
        elif opcao==3:
            a = int( input('Digite numero a: ') )
            b = int( input('Digite numero b: ') )
            print(f'O produto de {a} e {b} é {Produto(a,b)}\n')
        elif opcao==4:
            a = int( input('Digite numero a: ') )
            b = int( input('Digite numero b: ') )
            print(f'A Divisão de {a} e {b} é {Divisao(a, b)}\n')
        elif opcao==5:
            break
menu()