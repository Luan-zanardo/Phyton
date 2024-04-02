#var
salariomensal = float(input("Digite seu salário mensal:"))
produtovendido= input("Escolha o produto que você vendeu a, b ou c :")
quantidade= int(input("Digite a quantidade de produtos que você vendeu: "))

# calcular o produto vendido

if produtovendido == "a":
    produtofinal= quantidade * 5
    comissao = produtofinal * 0.05
    print("Sua comisão é", comissao)

if produtovendido == "b":
    produtofinal= quantidade * 10
    comissao = produtofinal * 0.10
    print("Sua comissão é:", comissao)

if produtovendido == "c":
    produtofinal= quantidade * 15
    comissao= produtofinal * 0.05
    print("Sua comissão é:", comissao)

salariofinal = (salariomensal + comissao)
print("Seu salário final é:", salariofinal)

print("O produto vendido foi:", produtovendido,"O valor da venda foi:", produtofinal,"O lucro final dele foi", salariofinal)


