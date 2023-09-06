"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
de aumento."""

preco = float(input("Digite preço do produto: "))

aumento = preco + ((15 / 100)* preco)
desconto = preco - ((5 / 100)* preco)

print(f"preço original {preco}R$")
print(f"preço com 15% de aumento: {round(aumento, 2)}R$")
print(f"preço com 5% de desconto: {round(desconto, 2)}R$")