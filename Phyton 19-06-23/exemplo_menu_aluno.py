#variaveis globais (todo programa)
codigo = []
nome   = []
idade  = []
status = []
i      = 0

def ListaAlunos():
    if (i==0):
        print("Nenhum Aluno no Sistema !!!")
    else:
        print("----------------- Listar --------------")
        print("Código\tNome\tIdade\tStatus")
        for x in range (len(codigo)):
            if (status[x]=="Ativo"):
                print(codigo[x],nome[x],idade[x],status[x])
    print("-------------------------------------------")

def CadAlunos():
    print("----------------- Cadastrar --------------")
    global i
    i += 1
    print("O Código do Aluno vai ser ",i)
    codigo.append(i)
    status.append("Ativo")
    nome.append(input("Digite o nome do aluno : "))
    idade.append(int(input("Digite idade do aluno :")))
    print("------------------------------------------")

def ExcAluno():
    print("----------------- Excluir ----------------")
    global i
    if (i==0):
        print("Nenhum Aluno no sistema !!!")
    else:
        auxcodigo = int(input("Código Aluno para Excluir : "))
        encontrado = False
        for x in range(len(codigo)):
            if (auxcodigo == codigo[x]):
                codigo.pop(x)
                nome.pop(x)
                idade.pop(x)
                i -= 1
                encontrado = True
        if (encontrado==False):
            print("Nenhum aluno encontrado para excluir !!!")
        print("----------------------------------------")

def InativarAluno():
    print("----------------- Inativar --------------")
    if (i==0):
        print("Nenhum Aluno no sistema !!!")
    else:
        auxcodigo = int(input("Código Aluno para Inativar : "))
        encontrado = False
        for x in range(len(codigo)):
            if (auxcodigo == codigo[x]):
                status[x]  = "Inativar"
                encontrado = True
        if (encontrado==False):
            print("Nenhum aluno encontrado para inativar !!!")
    print("---------------------------------------")

#procedimento MENU
def main():
    while True:
        op = int(input("1 - Cadastro de Aluno"
                       "\n2 - Lista de Alunos"
                       "\n3 - Exluir Aluno"
                       "\n4 - Inativar Aluno"
                       "\n5 - Sair "
                       "\n Escolha sua opção: "))
        if (op==1):
            CadAlunos()
        if (op==2):
            ListaAlunos()
        if (op==3):
            ExcAluno()
        if (op==4):
            InativarAluno()
        if (op==5):
            break

#principal
main()