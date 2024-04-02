'''Leia a idade e o tempo de servicio de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos'''

idade = int(input("Digite idade: "))
tempotrabalho = int(input("Digite tempo de trabalho: "))

if(idade >= 65 or tempotrabalho >= 30 or idade >= 60 and tempotrabalho >= 25):
    print(f"Você tem {idade} anos de idade e {tempotrabalho} anos de trabalho, pode se aposentar")