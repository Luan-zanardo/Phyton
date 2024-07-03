opcao = "S"

while(opcao == "S"):
    nota = float(input("Digite nota: "))
    if nota < 0 or nota > 10:
        print ("Nota invalida, deve estar entre 0 e 10")
    opcao = input("Deseja cadastrar mais notas, S ou N: ")
    if(opcao == "N"): #condição para parar repetição
        break