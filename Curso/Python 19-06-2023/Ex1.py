alunos = []
cursos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    aluno = {"nome": nome, "idade": idade}
    alunos.append(aluno)

def cadastrar_curso():
    nome = input("Digite o nome do curso: ")
    periodo = input("Digite o período do curso (matutino, vespertino ou noturno): ")
    curso = {"nome": nome, "periodo": periodo}
    cursos.append(curso)

def contar_alunos_por_idade():
    if len(alunos) == 0:
        print("Não há alunos cadastrados.")
        return

    menor_idade = alunos[0]["idade"]
    maior_idade = alunos[0]["idade"]

    for aluno in alunos:
        idade = aluno["idade"]
        if idade < menor_idade:
            menor_idade = idade
        if idade > maior_idade:
            maior_idade = idade

    print(f"Número de alunos maior de idade: {len([aluno for aluno in alunos if aluno['idade'] >= 18])}")
    print(f"Número de alunos menor de idade: {len([aluno for aluno in alunos if aluno['idade'] < 18])}")

def contar_cursos_por_periodo():
    if len(cursos) == 0:
        print("Não há cursos cadastrados.")
        return

    periodos = {"matutino": 0, "vespertino": 0, "noturno": 0}

    for curso in cursos:
        periodo = curso["periodo"]
        if periodo in periodos:
            periodos[periodo] += 1

    for periodo, quantidade in periodos.items():
        print(f"Número de cursos no período {periodo}: {quantidade}")

def exibir_menu():
    print("\n---- MENU ----")
    print("1. Cadastrar aluno")
    print("2. Cadastrar curso")
    print("3. Verificar número de alunos por idade")
    print("4. Verificar número de cursos por período")
    print("5. Sair")

exibir_menu()

while True:
    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        cadastrar_curso()
    elif opcao == "3":
        contar_alunos_por_idade()
    elif opcao == "4":
        contar_cursos_por_periodo()
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")

    exibir_menu()