"""Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e mostre os itens repetidos. """

from itertools import count

lista = []
repetido = []

for i in range(5):
    item = input("Digite item: ")
    lista.append(item)
    if(lista.count(item) == 2):
        repetido.append(item)

print(f"itens adicionados na lista: {lista}")
print(f"itens adicionados repetidos: {repetido}")