'''26) Faça um algoritmo para ler as 3 notas obtidas por um aluno nas 3 verificações 
e a média dos exercícios que fazem parte da avaliação. Calcular a média de aproveitamento,
usando a fórmula abaixo e escrever o conceito do aluno de acordo com a tabela de conceitos mais abaixo:'''

nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
nota3 = float(input("Digite nota 3: "))
mediaexercicios = float(input("Digite a media dos exercícios: "))

mda = (nota1 + nota2 * 2 + nota3 * 3 + mediaexercicios) / 7

if(mda >= 9):
    print(f"média: {mda}, conceito: A")
elif(mda >= 7.5 & mda < 9):
    print(f"média: {mda}, conceito: B")
elif(mda >= 6& mda < 7.5):
    print(f"média: {mda}, conceito: C")
elif(mda < 6):
    print(f"média: {mda}, conceito: D")