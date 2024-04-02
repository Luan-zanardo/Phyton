'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do
usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

def Menu():
    while True:
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")

        if(nome == senha):
            print("Erro! sua senha está igual ao nome de usuário")
        else:
            print("Logado com sucesso!")
            break
Menu()

