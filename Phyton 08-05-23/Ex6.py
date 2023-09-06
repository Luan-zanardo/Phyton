import random    #chamar biblioteca numeros randomicos

#funcao gerar numero aleatorio entre (1 e 6)
def gerar_valor():
    return random.randint(1,6)

#funcao repetir nr vezes (jogar dados)
def repete(numero):
    teste1 = teste2 = teste3 = teste4 = teste5 = teste6 = 0
    for val in range(numero):
        teste = gerar_valor()
        if (teste == 1):
            teste1 += 1
        elif (teste == 2):
            teste2 += 1
        elif (teste == 3):
            teste3 += 1
        elif (teste == 4):
            teste4 += 1
        elif (teste == 5):
            teste5 += 1
        else:
            teste6 += 1
    print("Numero 1 saiu ", teste1, " vezes = ", (teste1 / numero) * 100, " %")
    print("Numero 2 saiu ", teste2, " vezes = ", (teste2 / numero) * 100, " %")
    print("Numero 3 saiu ", teste3, " vezes = ", (teste3 / numero) * 100, " %")
    print("Numero 4 saiu ", teste4, " vezes = ", (teste4 / numero) * 100, " %")
    print("Numero 5 saiu ", teste5, " vezes = ", (teste5 / numero) * 100, " %")
    print("Numero 6 saiu ", teste6, " vezes = ", (teste6 / numero) * 100, " %")

#principal
numero = int(input('Quantos lançamentos deseja? '))
repete(numero)
