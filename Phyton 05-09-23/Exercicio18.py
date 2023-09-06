'''Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.'''

a = float(input("Digite a primeira nota de 0 a 5: "))
b = float(input("Digite a segunda nota de 0 a 5: "))
c = float(input("Digite a terceira nota de 0 a 10: "))

media = (a + b + c) / 2

if(media >= 6):
    print(f"Aluno foi aprovado com média {round(media, 2)}")
else:
    print(f"Aluno foi reprovado com média {round(media, 2)}")