"""Faça um script que leia dois números e retorne como resultado a soma deles. Faça um script que leia algo
pelo teclado e mostra na tela o seu tipo de dado."""

a = int(input("Digite valor 1: "))
b = int(input("Digite valor 2: "))

soma = a + b
print(f"A soma dos valores é {soma}")

c = input("Digite algo: ")

print('o dado é uma letra?: ', c.isalpha())
print('o dado é numérico?: ', c.isnumeric())
print('o dado é só espaço?: ', c.isspace())
print('o dado é alfanumérico?: ', c.isalnum())
print('o dado é maiúsculo?: ', c.isupper())
print('o dado é minúsculo?: ', c.islower())
print('o dado é capitalizada?: ', c.istitle())