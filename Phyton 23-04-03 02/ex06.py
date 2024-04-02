dollar = float(input("Digite o valor atual do dollar: "))

verba = 150000 * dollar
preco = 1350 * dollar

pracas = verba / preco
sobra = verba % preco
print("O valor da verba em reais é de: ", verba, "R$")
print("O valor de cada praça em reais  é de: ", preco, "R$")
print("A quantidade de praças que podem ser contruidas são: ", pracas)
print("A quantia restante do dinheiro é de: ", sobra, "R$")