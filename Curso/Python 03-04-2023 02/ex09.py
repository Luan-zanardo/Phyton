nome = input("Digite seu nome: ")
saldo = float(input("Digite seu salário medio: "))

if (saldo  >= 0) and (saldo <= 2000):
    print(nome, "vc não possui saldo para Crédito")

if (saldo >= 2001) and (saldo <= 4000):
    print(nome, "vc possui 5% de Crédito")
    credito = saldo * 0.05
    print("Créditos de R$ = ", credito)

if (saldo >= 4001) and (saldo <= 6000):
    print(nome, "vc possui 10% de Crédito")
    credito = saldo * 0.1
    print("Créditos de R$ = ", credito)

if (saldo > 6000):
    print(nome, "vc possui 15% de Crédito")
    credito = saldo * 0.15
    print("Créditos de R$ = ", credito)