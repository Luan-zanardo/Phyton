valor = float(input("Digite o valor: "))
cotacao = float(input("Digite a cotação atual do Dolár U$: "))
opcao = input("Escolha a moeda D(dolar) ou R(reais): ")

#converter para dolares

if opcao == "D":
    total = valor / cotacao
    print ("valor em Doláres U$: ", total)

#converter para Reais

if opcao == "R":
    total = valor * cotacao
    print("Valor em R$: ", total)