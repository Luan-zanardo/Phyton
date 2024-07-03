#Função verificar positivo e negativo
def Verificar(valor):
    if(valor < 0):
        return False
    else:
        return True

#Principal
valor = int(input("Informe um numero: "))
resultado = Verificar(valor)
if resultado == True:
    print(f"o numero {valor} é negativo")
else:
    print(f"o numero {valor} é postivo")