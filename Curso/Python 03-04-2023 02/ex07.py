dinheiro = float(input("Digite o valor que deseja converter: "))
dollar = float(input("Digite o valor atual do dollar: "))
funcao = int(input("(1 - Converter R$ para US$) (2 - Converter US$ para R$) "))

if funcao == 1:
    conversao = dinheiro / dollar
    print(f"Você tem {conversao} dollars")

if funcao == 2:
    conversao = dinheiro * dollar
    print(f"Você tem {conversao} reais")
