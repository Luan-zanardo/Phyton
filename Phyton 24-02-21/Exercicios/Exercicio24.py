'''24) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
 Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível 
 (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo 
 cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90
'''

litros = int(input("Digite total de litros vendidos: "))

op = input("Escolha combustivel:\n"
               "A-álcool\n"
               "G-gasolina\n"
               "")
if(op == "A"):
    valor = litros * 2.90
    print(f"Litros: {litros}, Combustivel: Alcool, Preço p/ litro: 2.90, total: {valor}")
elif(op == "G"):
    valor = litros * 3.30
    print(f"Litros: {litros}, Combustivel: Gasolina, Preço p/ litro: 3.30, total: {valor}")