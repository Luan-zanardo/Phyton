atletas = []

def cadastrar_atleta():
    nome = input("Digite o nome do atleta: ")
    idade = int(input("Digite a idade do atleta: "))
    peso = float(input("Digite o peso do atleta: "))
    modalidade = input("Digite a modalidade do atleta: ")
    atleta = {"nome": nome, "idade": idade, "peso": peso, "modalidade": modalidade}
    atletas.append(atleta)

def contar_atletas_por_modalidade():
    if len(atletas) == 0:
        print("Não há atletas cadastrados.")
        return

    modalidades = {}

    for atleta in atletas:
        modalidade = atleta["modalidade"]
        if modalidade in modalidades:
            modalidades[modalidade] += 1
        else:
            modalidades[modalidade] = 1

    for modalidade, quantidade in modalidades.items():
        print(f"Número de atletas na modalidade {modalidade}: {quantidade}")

def contar_atletas_por_faixa_etaria():
    if len(atletas) == 0:
        print("Não há atletas cadastrados.")
        return

    faixas_etarias = {
        "De 18 a 25 anos": 0,
        "De 26 a 35 anos": 0,
        "De 36 a 45 anos": 0,
        "Acima de 45 anos": 0
    }

    for atleta in atletas:
        idade = atleta["idade"]
        if 18 <= idade <= 25:
            faixas_etarias["De 18 a 25 anos"] += 1
        elif 26 <= idade <= 35:
            faixas_etarias["De 26 a 35 anos"] += 1
        elif 36 <= idade <= 45:
            faixas_etarias["De 36 a 45 anos"] += 1
        else:
            faixas_etarias["Acima de 45 anos"] += 1

    for faixa_etaria, quantidade in faixas_etarias.items():
        print(f"Número de atletas na faixa etária {faixa_etaria}: {quantidade}")

def exibir_menu():
    print("\n---- MENU ----")
    print("1. Cadastrar atleta")
    print("2. Verificar número de atletas por modalidade")
    print("3. Verificar número de atletas por faixa etária")
    print("4. Sair")

exibir_menu()

while True:
    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        cadastrar_atleta()
    elif opcao == "2":
        contar_atletas_por_modalidade()
    elif opcao == "3":
        contar_atletas_por_faixa_etaria()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")

    exibir_menu()