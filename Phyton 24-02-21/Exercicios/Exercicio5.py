'''5) Faça um algoritmo que leia três notas de um aluno, calcule e escreva a 
média final deste aluno. 	Considerar que a média é ponderada e que o peso 
das notas é 2, 3 e 5. Fórmula para o cálculo da média final é:'''

nota1 = int(input("Digite nota 1: "))
nota2 = int(input("Digite nota 2: "))
nota3 = int(input("Digite nota 3: "))

soma = nota1 + nota2 + nota3

print(f"média do aluno: {soma / 3}")