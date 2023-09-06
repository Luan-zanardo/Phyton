totalinformatica = 0
totalmecatronica = 0
totaleletronica = 0
totaldesign = 0
contador = 1
for contador in range(5):
    nome = input("Digite nome aluno: ")
    print("Opções de curso: ")
    print("INF - Informatica ")
    print("MEC - Mecatrônica ")
    print("ELE - Eletrônica  ")
    print("DES - Design      ")
    curso = input("Escolha seu curso: ")
    if (curso == "INF"):
        totalinformatica = totalinformatica + 1
    if (curso == "MEC"):
        totalmecatronica = totalmecatronica + 1
    if (curso == "ELE"):
        totaleletronica = totaleletronica + 1
    if (curso == "DES"):
        totaldesign = totaldesign + 1
print ("Total de alunos curso Informática  : ",totalinformatica)
print ("Total de alunos curso Mecatrônica  : ",totalmecatronica)
print ("Total de alunos curso Eletrônica   : ",totaleletronica)
print ("Total de alunos curso Design       : ",totaldesign)
