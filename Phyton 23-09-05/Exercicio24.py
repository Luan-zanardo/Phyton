'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.'''

def Menu():
    while True:
        a = int(input("Digite uma nota de 0 a 10: "))
        if(a < 0 or a > 10):
            print("Informe um valor válido")
        else:
            print("Valor válido")
            break
Menu()