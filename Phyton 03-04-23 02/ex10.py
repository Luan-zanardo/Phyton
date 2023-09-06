nome = input("Digite nome: ")
salario = int(input("Digite salário: "))
print("Produtos Vendidos: ")
print("Produto A")
print("Produto B")
print("Produto C")
produto = int(input("Escolha produto: "))
quantidade = int(input("Digite quantidade: "))

if(produto == 1):
    totalvendas = quantidade * 5
    comissao = totalvendas * 0.05
    print("Funcionario: ", nome, "Comissão R$", comissao)

if(produto == 2):
    totalvendas = quantidade * 10
    comissao = totalvendas * 0.10
    print("Funcionario: ", nome, "Comissão R$", comissao)

if(produto == 3):
    totalvendas = quantidade * 15
    comissao = totalvendas * 0.15
    print("Funcionario: ", nome, "Comissão R$", comissao)