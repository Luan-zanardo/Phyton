"""Escreva um Programa que verifique se um elemento está na lista e verifique a posição exata dele da lista."""

from itertools import count

lista = ["uno", "corsa", "gol", "golf"]

print(lista)
print("Digite algum elemento que esta lista: ")

for i in range(5):
    item = input("Digite item: ")
    if(lista.count(item)):
        print(f"O item que você digitou esta na posição {lista.index(item)} da lista")