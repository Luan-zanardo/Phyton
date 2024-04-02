'''Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).'''

while True:
    nome = input("Digite seu nome: ")
    if(len(nome) > 3):
        print("Informação inserida com Sucesso!")
        break
    else:
        print("Inválido, seu nome precissa ter mais de 3 caracteres.")

while True:
    idade = int(input("Digite sua idade: "))
    if(idade >= 0 and idade <= 150):
        print("Informação inserida com Sucesso!")
        break
    else:
        print("Inválido, você só pode ter entre 0 a 150 anos.")

while True:
    salario = int(input("Digite seu salário: "))
    if(salario > 0):
        print("Informação inserida com Sucesso!")
        break
    else:
        print("Inválido, seu salário precissa ser maior que 0.")
while True:
    sexo = input("Digite seu sexo, (f) para feminino e (m) para masculino: ")
    if(sexo == "f" or sexo == "m"):
        print("Informação inserida com Sucesso!")
        break
    else:
        print("Inválido, esse sexo não existe.")
while True:
    estadocivil = input("Digite seu estado civil, (s) solteiro, (c) casado, (v) viuva, (d) divorciado: ")
    if(estadocivil == "s" or estadocivil == "c" or estadocivil == "v" or estadocivil == "d"):
        print("Informação inserida com Sucesso!")
        break
    else:
        print("Inválido, esse estado civil não existe.")

print("Sucesso! Todas informações estão validadas.")