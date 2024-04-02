valor1 = int(input("Digite valor 1: "))
valor2 = int(input("Digite valor 2: "))
valor3 = int(input("Digite valor 3: "))

media = (valor1 + valor2 + valor3) / 3

if(valor1 > valor2) and (valor1 > valor3):
    print(f"valor 1({valor1}) é maior")
if(valor2 > valor1) and (valor2 > valor3):
    print(f"valor 2({valor3}) é maior")
if(valor3 > valor1) and (valor3 > valor2):
    print(f"valor 3({valor3}) é maior")

if(valor1 < valor2) and (valor1 < valor3):
    print(f"valor 1({valor1}) é menor")
if(valor2 < valor1) and (valor2 < valor3):
    print(f"valor 2({valor2}) é menor")
if(valor3 < valor1) and (valor3 < valor2):
    print(f"valor 3({valor3}) é menor")

print("a media dos 3 valores é: ", media)


