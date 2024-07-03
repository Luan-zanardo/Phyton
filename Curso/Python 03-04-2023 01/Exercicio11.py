#repeticao
totalFundamental = 0
totalMedio = 0
totalTecnico = 0
totalGraduacao = 0
contador = 0

#entrada dados
while contador <= 5:
    nome = input("Digite nome vendedor: ")
    print("Escolha sua formação: ")
    print("1 - Ensino Fundamental")
    print("2 - Ensino Médio")
    print("3 - Ensino Técnico")
    print("4 - Graduação")
    opcao = int(input("Escolha formação: ")) #converter integer

    if(opcao == 1):
        print(f"Aluno: {nome}, Formação {opcao}, Ensino Fundamental")
        totalFundamental += 1
    if(opcao == 2):
        print(f"Aluno: {nome}, Formação {opcao}, Ensino Médio")
        totalMedio += 1
    if(opcao == 3):
        print(f"Aluno: {nome}, Formação {opcao}, Ensino Técnico")
        totalTecnico += 1
    if(opcao == 4):
        print(f"Aluno: {nome}, Formação {opcao}, Graduação")
        totalGraduacao += 1

    contador += 1
    if(contador == 5):
        break

print ("Total de aluno Ensino Fundamental: ", totalFundamental)
print ("Total de aluno Ensino Médio: ", totalMedio)
print ("Total de aluno Ensino Técnico: ", totalTecnico)
print ("Total de aluno Graduação: ", totalGraduacao)
