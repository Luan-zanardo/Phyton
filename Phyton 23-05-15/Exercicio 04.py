def Verificar(altura, sexo):
    if sexo == "M"
        pesoIdeal = (72.7 * altura) - 58

    if sexo == "F"
        pesoIdeal = (62.1 * altura) - 44.7
    return pesoIdeal

nome = input("Digite seu nome: ")
altura = float(input("Digite a sua altura: "))
print("F - Feminino, M - Masculino")
sexo = input("Digite seu sexo: ")
resultado = Verificar(altura, sexo)
print(f"{nome}, {resultado}")