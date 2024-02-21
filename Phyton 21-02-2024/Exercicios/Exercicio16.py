'''16) Reescreva o exercício anterior utilizando a estrutura While.'''

valor1 = int(input("Digite valor 1: "))
valor2 = int(input("Digite valor 2: "))
while True:
    if(valor2 == 0):
        valor2 = int(input("Digite valor 2: "))
    else:
        break

divisao = valor1 / valor2

print(f"{valor1} / {valor2}: {divisao}")