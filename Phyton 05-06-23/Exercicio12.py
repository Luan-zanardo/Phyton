valores = []
 
maior = 0
menor = float('inf')

#Contador para receber valores
print("Digite 5 valores aleatorios abaixo!")
for cont in range (5):
    valor = float(input("Digite um valor: "))
    valores.append(valor)
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

media = sum(valores)/ len(valores)
print("Todos valores registrados: ",valores)
print("Menor valor registrado: ",menor)
print("Maior valor registrado: ",maior)
print("Média dos valores: ",media)
