#funcao converter Farenheit
def ConverterFAR(tempC):
    totalF = (tempC * 9/5) + 32
    return totalF

#funcao converter Celsius
def ConverterCEL(tempF):
    totalC = (tempF - 32)*5/9
    return totalC

#procedimento menu
def menu():
    while True:
        opcao = int(input('Digite 1. Converter Celsius para Farenheit: \n' +
                          'Digite 2. Converter Farenheit para Celsius: \n' +
                          'Digite 3. Sair'))

        if opcao==1:
            tempC = int( input('Graus Celsius: ') )
            print('Convertido: ', ConverterFAR(tempC),' graus Farenheit\n')
        elif opcao==2:
            tempF = int( input('Graus Farenheit: ') )
            print('Convertido: ', ConverterCEL(tempF),' graus Celsius\n')
        elif opcao==3:
            break

#programa principal
menu()