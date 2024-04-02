'''8) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga 
se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).'''

atual = int(input("Ano atual: "))
nascimento = int(input("Ano de nascimento: "))

idade = atual - nascimento

if(idade >= 18):
    print(f"idade: {idade}, pode votar!")
else:
    print(f"idade: {idade}, não pode votar!")