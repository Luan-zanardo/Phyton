'''Elabore um programa que leia o nome do usuário e mostre o nome de traz para frente, utilizando somente letras maiúsculas.'''

nome = input("Digite nome: ")
nomeInvertido = nome.upper()[::-1]

print("Seu nome ao contrário em letras maiúsculas é:", nomeInvertido)