#contadores por cargo
totalanalista = 0
totalprogramador = 0
totalgerente = 0
totalgeral = 0
contador = 1
#pergunta total deseja cadastrar (contador)
nrfuncionarios = int(input("Quantos deseja cadastrar?"))
#repeticao
for contador in range(nrfuncionarios):
    #entrada de dados
    nome = input("Digite nome funcionário: ")
    salario = float(input("Digite o salário R$: "))
    print("Escolha seu cargo: ")
    print("1 - Analista ")
    print("2 - Programador ")
    print("3 - Gerente")
    cargo = int(input("Escolha seu cargo: "))
    if (cargo == 1):
        totalanalista = totalanalista + salario
    if (cargo == 2):
        totalprogramador = totalprogramador + salario
    if (cargo == 3):
         totalgerente = totalgerente + salario

#mostrar o total de cada formacao
print ("Total de salários do cargo Analista   : ",totalanalista)
print ("Total de salários do cargo Programador: ",totalprogramador)
print ("Total de salários do cargo Gerente    : ",totalgerente)
totalgeral = totalanalista + totalprogramador + totalgerente
print ("Total Geral R$ : ",totalgeral)
