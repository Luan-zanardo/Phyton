"""Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode
comprar. Considere: US$ 1.00 = R$ 5.41"""

real = float(input("Digite quantidade de dinheiro que você tem na carteira: "))

dollar = real / 5.41

print(f"Com {real} reais, você pode comprar {round(dollar, 2)} dollars")