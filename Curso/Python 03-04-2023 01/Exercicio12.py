tinformatica = 0
tmecatronica = 0
teletronica = 0
tdesign = 0
contador = 1

for contador in range(5):
    nome = input("Digite o nome aluno: ")
    print("Escolha seu curso: ")
    print("1 - Informatica")
    print("2 - Mecatronica")
    print("3 - Eletronica")
    print("4 - Design")
    curso = int(input("Digite seu curso: "))

    if(curso == 1):
        tinformatica += 1
    if (curso == 2):
        tmecatronica += 1
    if (curso == 3):
        teletronica += 1
    if (curso == 4):
        tdesign += 1

print("Total de alunos de Informatica: ", tinformatica)
print("Total de alunos de Mecatronica: ", tmecatronica)
print("Total de alunos de Eletronica: ", teletronica)
print("Total de alunos de Desing: ", tdesign)
