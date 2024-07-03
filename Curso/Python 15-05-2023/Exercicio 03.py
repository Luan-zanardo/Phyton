
def Verificar(media):
    if(media >= 0) & (media <= 4.9):
       conceito = "D"
    if(media >= 5) & (media <= 6.9):
        conceito = "C"
    if(media >= 7) & (media <= 8.9):
        conceito = "B"
    if(media >= 9) & (media <= 10):
        conceito = "A"
    return  conceito

nome = input("Digite nome aluno: ")
media = float(input("Digite a média final: "))
resultado = Verificar(media)
print(f"Aluno {nome}, Conceito final: {resultado}")