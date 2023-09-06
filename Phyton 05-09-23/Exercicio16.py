'''Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit para Celsius 
ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida conversão'''

def ConverterFAR(tempC):
    totalF = (tempC * 9/5) + 32
    return totalF

def ConverterCEL(tempF):
    totalC = (tempF - 32)*5/9
    return totalC

def menu():
    while True:
        opcao = int(input('1 - Converter Celsius para Farenheit\n' +
                          '2 - Converter Farenheit para Celsius\n' +
                          '3 - Sair\n'))
        if opcao==1:
            tempC = int( input('Graus Celsius: ') )
            print('Convertido: ', ConverterFAR(tempC),' graus Farenheit\n')
        elif opcao==2:
            tempF = int( input('Graus Farenheit: ') )
            print('Convertido: ', ConverterCEL(tempF),' graus Celsius\n')
        elif opcao==3:
            break
menu()