"""Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre ele."""

dado = input('Informe um dado: ')
print('o dado é uma letra?: ', dado.isalpha())
print('o dado é numérico?: ', dado.isnumeric())
print('o dado é só espaço?: ', dado.isspace())
print('o dado é alfanumérico?: ', dado.isalnum())
print('o dado é maiúsculo?: ', dado.isupper())
print('o dado é minúsculo?: ', dado.islower())
print('o dado é capitalizada?: ', dado.istitle())