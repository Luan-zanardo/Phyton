'''14) Ler dois valores e imprimir uma das três mensagens a seguir:
‘Números iguais’, caso os números sejam iguais
‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
‘Segundo maior’, caso o segundo seja maior que o primeiro.'''

valor1 = int(input("Digite valor 1: "))
valor2 = int(input("Digite valor 2: "))

if(valor1 == valor2):
    print("valores iguais!")
elif(valor1 > valor2):
    print("valor 1 maior que valor 2")
elif(valor1 < valor2):
    print("valor 2 maior que valor 1")