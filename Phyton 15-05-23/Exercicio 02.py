def Verificar(valor):
    if(valor % 2)==0:
        return False
    else:
        return True

valor = int(input("Informe um numero: "))

resultado = Verificar(valor)

if resultado == True:
    print(f"o numero {valor} é ímpar")
else:
    print(f"o numero {valor} é par")