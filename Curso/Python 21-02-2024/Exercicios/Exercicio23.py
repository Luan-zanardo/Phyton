'''23) Escreva um algoritmo para ler 8 números. Todos os números lidos com valor inferior a 
40 devem ser somados. Escreva o valor final da soma efetuada.'''

lista = []

for i in range(8):
    valor = float(input(f"Digite o {i+1}º valor: "))
    if (valor < 40):
        lista.append(valor)

print(f"lista: {lista}, valores somados: {sum(lista)}")