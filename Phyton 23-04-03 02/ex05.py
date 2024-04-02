nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
sexo = input("Digite (F) para Feminino e (M) para Masculino): ")

if sexo == "M":
    pesoideal = (72.7 * altura) - 58
    print(nome, "seu peso ideal é: ", pesoideal)

if sexo == "F":
    pesoideal = (62.1 * altura) - 44.7
    print(nome, "seu peso ideal é: ", pesoideal)
