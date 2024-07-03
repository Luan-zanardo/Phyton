dolaratual= float(input("Digite o Dólar atual:"))
valorpraca= float(input("digite o valor de cada praça:"))
valortodo= float(input("digite o valor total recebido do governo:"))

Valorbr = (valortodo * dolaratual)
print("o valor total para verba é:", Valorbr)

Valorpracabr = (valorpraca * dolaratual)
print(" o valor para a contrução de cada praça é:", Valorpracabr)

obraspraca = (Valorbr / Valorpracabr)
print(" serão contruidas:", round(obraspraca))

