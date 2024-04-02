numero = int(input("Digite um numero: "))
for contador in range(10):
    total = numero * (contador + 1) #calcula a multiplicação
    print("Tabuada = ", numero, "x", contador + 1, " = ", total)