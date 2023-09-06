#var
valor1 = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))
valor3 = float(input("Digite o valor 3: "))

#verificar maior

if (valor1 > valor2) and (valor1 > valor3):
 print(valor1, "É o maior número!")

if (valor2 > valor1) and (valor2 > valor3):
     print(valor2, "É o maior número!")

if (valor3 > valor1) and (valor3 > valor2):
     print(valor3, "É o maior número!")

#verificar o menor numero

if (valor1 < valor2) and (valor1 < valor3):
 print(valor1, "É o menor número!")

if (valor2 < valor1) and (valor2 < valor3):
     print(valor2, "É o menor número!")

if (valor3 < valor1) and (valor3 < valor2):
     print(valor3, "É o menor número!")

# verficar a média

media = (valor1 + valor2 + valor3)/3
print("A média dos valores é:", media)


