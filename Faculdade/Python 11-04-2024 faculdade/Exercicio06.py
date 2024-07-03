
litros = int(input("Quantidade de litros vendidos: "))
op = input("Digite:\n"
           "(G) -> para Gasolina\n"
           "(A) -> para Alcool\n").upper()

def combustivelValue(porcent, preco, combustivel):
    preco = (20 * preco)
    desconto = preco * (porcent/100)
    total = preco - desconto
    print(f"Tipo de combustivel: {combustivel}\n"
          f"Litros: {litros}\n" 
          f"Preco bruto: {round(preco, 2)} R$\n"
          f"Desconto de {porcent}%: {round(desconto, 2)} R$\n"
          f"Preco total: {round(total, 2)}")

if(op == "G"):
    if(litros <= 20 ):
        combustivelValue(4, 5.57, "Gasolina")
    elif(litros > 20):
        combustivelValue(6, 5.57, "Gasolina")
if(op == "A"):
    if(litros <= 20 ):
        combustivelValue(2, 4.98, "Alcool")
    elif(litros > 20):
        combustivelValue(5, 4.98, "Alcool")