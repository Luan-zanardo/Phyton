#função calcular temperatura em para Farenheit
def ConverterCEL(tempF):
    totalC = (tempF - 32) * 5/9
    return totalC

#função calcular temperatura pra Celsius
def ConverterFAR(tempC):
    totalF = (tempC * 9/5) + 32
    return totalF

def menu():
    while True:
        opcao = int(input("Digite 1. Converter Celsius para Fernheit \n"
                          "Digite 2. Converter Fernheit para Celsius \n"
                          "Digite 3. Sair\n"))
        if (opcao == 1):
            tempC = int(input("Graus Celsius: "))
            print("Convertido: ", ConverterFAR(tempC), "Graus Ferenheit \n")
        elif(opcao == 2):
            tempF = int(input("Graus Farenheit: \n"))
            print("Convertido: ", ConverterCEL(tempF), "Graus Ferenheit \n")
        elif(opcao == 3):
            break

menu()

#programa principal
#temperaturaF = int(input("Digite temperatura em Graus Celsius: "))
#print("Temperatura Convertida: ", ConverterCEL(temperaturaF), "graus Farenheit\n")
#temperaturaC = int(input("Digite temperatura em Graus Farenheit: "))
#print("Temperatura Convertida: ", ConverterCEL(temperaturaC), "graus Celsius\n")
