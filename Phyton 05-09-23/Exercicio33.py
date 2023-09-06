'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os
códigos utilizados são:
 1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o
valor zero.'''

jose = 0
joao = 0
maria = 0
claudio = 0
nulo = 0
branco = 0

def Resultados():
    total = jose + joao + maria + claudio + nulo + branco

    print("Quantidade de votos: ")
    print(f"José: {jose} votos")
    print(f"João: {joao} votos")
    print(f"Maria: {maria} votos")
    print(f"Cláudio: {claudio} votos")
    print(f"Nulo: {nulo} votos")
    print(f"Branco: {branco} votos")
    print(f"Percentagem de votos nulos sobre o total de votos: {round(((nulo / total) * 100), 2)}%")
    print(f"Percentagem de votos em branco sobre o total de votos: {round(((branco / total) * 100), 2)}%")

def Menu():
    while True:
        global jose
        global joao
        global maria
        global claudio
        global nulo
        global branco

        opcao = int(input('1 - Jose\n' +
                                '2- João\n' +
                                '3 - Maria\n' +
                                '4 - Cláudio\n' +
                                '5 - Nulo\n' +
                                '6 - Branco\n' +
                                '7 - Sair\n' ))
        if opcao==1:
            jose += 1
        elif opcao==2:
            joao += 1
        elif opcao==3:
            maria += 1
        elif opcao==4:
            claudio += 1
        elif opcao==5:
            nulo += 1
        elif opcao==6:
            branco += 1
        elif opcao==7:
            Resultados()
            break
Menu()