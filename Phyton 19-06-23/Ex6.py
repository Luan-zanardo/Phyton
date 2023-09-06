MAX_FUNCIONARIOS = 50

def cadastrar_funcionario(funcionarios):
    if len(funcionarios) >= MAX_FUNCIONARIOS:
        print("Número máximo de funcionários atingido.")
        return

    codigo = input("Digite o código do funcionário: ")
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    setor = input("Digite o setor do funcionário (Producao/PCP/Adm/TI): ")

    while setor not in ["Producao", "PCP", "Adm", "TI"]:
        print("Setor inválido. Digite novamente.")
        setor = input("Digite o setor do funcionário (Producao/PCP/Adm/TI): ")

    funcionario = {
        "codigo": codigo,
        "nome": nome,
        "salario": salario,
        "setor": setor
    }

    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso.")

def mostrar_funcionarios_por_setor(funcionarios, setor):
    funcionarios_setor = [funcionario for funcionario in funcionarios if funcionario["setor"] == setor]

    if len(funcionarios_setor) == 0:
        print(f"Nenhum funcionário encontrado no setor {setor}.")
        return

    print(f"Funcionários do setor {setor}:")
    for funcionario in funcionarios_setor:
        print("Código:", funcionario["codigo"])
        print("Nome:", funcionario["nome"])
        print("Salário:", funcionario["salario"])
        print("-" * 20)

funcionarios = []

while True:
    print("1 - Cadastrar funcionário")
    print("2 - Mostrar funcionários por setor")
    print("3 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastrar_funcionario(funcionarios)
    elif opcao == "2":
        setor = input("Digite o setor para pesquisar os funcionários: ")
        mostrar_funcionarios_por_setor(funcionarios, setor)
    elif opcao == "3":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Digite novamente.")