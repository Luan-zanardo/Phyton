#contadores
totalFundamental = 0
totalmedio = 0
totaltecnico = 0
totalgraduacao = 0
contador = 1
#repeticao
for contador in range(5):
    #entrada de dados
    nome = input("Digite nome aluno: ")
    print("Escolha sua formação: ")
    print("1 - Ensino Fundamental ")
    print("2 - Ensino Medio ")
    print("3 - Ensino Técnico")
    print("4 - Gradução")
    opcao = int(input("Escolha formação: "))  #converter integer

    #verificar formacao
    if (opcao == 1):
        print ("Aluno: ",nome," Formação: ",opcao," Ensino Fundamental")
        totalFundamental = totalFundamental + 1 #acumulando o contador
    if (opcao == 2):
        print ("Aluno: ",nome," Formação: ",opcao," Ensino Médio")
        totalmedio = totalmedio + 1
    if (opcao == 3):
        print("Aluno: ", nome, " Formação: ",opcao," Ensino Técnico")
        totaltecnico= totaltecnico + 1
    if (opcao == 4):
        print("Aluno: ", nome, " Formação: ",opcao," Graduação")
        totalgraduacao = totalgraduacao + 1

#mostrar o total de cada formacao
print ("Total de aluno Ensino fundamental: ",totalFundamental)
print ("Total de aluno Ensino Médio      : ",totalmedio)
print ("Total de aluno Ensino Técnico    : ",totaltecnico)
print ("Total de aluno Ensino Graduacao  : ",totalgraduacao)
