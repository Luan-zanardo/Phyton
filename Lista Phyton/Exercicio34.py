'''Faça 4 listas:
A. Filmes
B. Jogos
C. Livros
D. Esporte
a. Adicione no mínimo 2 itens em cada lista.
b. Crie uma lista das 4 listas criadas acima.
c. Acesse (mostrar) algum item da lista livros.
d. Remova um item da lista esporte.'''

filmes = [ "Tropa de Elite", "Toy Story" ]
jogos = [ "Cuphead", "Counter Strike"]
livros = [ "Dom Quixote", "Guerra e Paz"]
esporte = [ "Futebol" , "Volêi"]

print(filmes)
print(jogos)
print(livros)
print(esporte)

lista = filmes + jogos + livros + esporte
print(lista)
print(livros[1])
del esporte[1]
print(esporte)