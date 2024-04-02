'''7) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e 
escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou 
maior que 6 o aluno é aprovado). Escrever também a média calculada.'''

avaliacao1 = int(input("Digite avaliação 1: "))
avaliacao2 = int(input("Digite avaliação 2: "))

media = (avaliacao1 + avaliacao2) / 2

if(media >= 6):
    print(f"Nota: {media}, aprovado!")
else:
    print(f"Nota: {media}, reprovado!")