#var
nome = (input("Digite seu nome: "))
saldomedio = (float(input("Digite seu saldo médio: ")))

# mostrar as opções e calcular

if (saldomedio> 0) and (saldomedio<=2000):
    print("Seu saldo não te permite ter créditos!")

if (saldomedio>2001) and (saldomedio<=4000):
    novosaldo = saldomedio + saldomedio * 0.05
    print ("Seu novo saldo é:", novosaldo)

if (saldomedio>4001) and (saldomedio<=6000):
    novosaldo = saldomedio + saldomedio * 0.10
    print("Seu novo saldo é:", novosaldo)

if (saldomedio>6001):
    novosaldo = saldomedio + saldomedio * 0.15
    print("Seu novo saldo é:", novosaldo)

