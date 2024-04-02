'''17) Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um aluno, calcule e imprima 
a média (simples) desse aluno. Só devem ser aceitos valores válidos durante a leitura 
(0 a 10) para cada nota.'''

while True:
    nota1 = float(input("Digite a nota da 1ª avaliação (0 a 10): "))
    if 0 <= nota1 <= 10:
        break
    else:
        print("Nota inválida. Digite uma nota entre 0 e 10.")

while True:
    nota2 = float(input("Digite a nota da 2ª avaliação (0 a 10): "))
    if 0 <= nota2 <= 10:
        break
    else:
        print("Nota inválida. Digite uma nota entre 0 e 10.")

media = (nota1 + nota2) / 2
print("A média do aluno é:", media)