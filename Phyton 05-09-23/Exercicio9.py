"""Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
Euros"""

nome = input("Digite nome: ")
real = float(input("Digite quantidade de dinheiro: "))

dollar = real / 5.41
euro = real / 5.44

print(f"Com {real} reais {nome} pode comprar {round(dollar, 2)} dollars ou {round(euro, 2)} euros")