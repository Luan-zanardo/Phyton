"""Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²."""

altura = float(input("Digite altura: "))
largura = float(input("Digite largura: "))

m = altura * largura
tinta = m / 2

print(f"São necessário {tinta} litros de tinta para pintar uma parede de {m} metros quadrados ")