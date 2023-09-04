"""Faça um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

metros = int(input("Digite um valor em metros: "))

centímetros = metros * 100
milímetros = metros * 1000

print(f"{metros} metros equivalem a {centímetros} centímetros")
print(f"{metros} metros equivalem a {milímetros} milímetros")