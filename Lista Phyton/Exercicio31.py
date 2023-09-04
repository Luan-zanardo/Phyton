'''Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo.'''

import random


def Menu():
    while True:
        escolha = input("Escolha Par (P) ou Ímpar (I): ")
        jogador = int(input("Digite um número: "))
        computador = random.randint(1, 10)
        
        print(f"Computador escolheu o número: {computador}")
        
        soma = jogador + computador
        
        print(f"Soma: {soma}")
        
        if (soma % 2 == 0 and escolha == "P"):
            print("Você venceu!")
        elif (soma % 2 != 0 and escolha == "I"):
            print("Você venceu!")
        else:
            print("Você perdeu!")
            break
Menu()