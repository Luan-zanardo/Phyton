#Funcao para ler os valores
def valor_par():
    while True:
        valor = int(input("Digite um valor inteiro par: "))
        if valor %2 == 0:
            return valor
        else:
            print("O valor digitado nao atende o que foi pedido! ")

#Criar vetor
valores = []

#Contador para ler os 6 valores
for cont in range (6):
    valor = valor_par()
    valores.append(valor)

#Mostrar os resultador na ordem inversa
print("Valores escritos na ordem inversa: ")
for i in range (5, -1, -1):
    print(valores[i])
