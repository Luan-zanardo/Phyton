"""Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 
2% de INSS. E ao final mostrar seu nome e salário final calculado."""

nome = input("Digite nome: ")
horastrabalhadas = int(input("Digite quantidade de horas trabalhadas: "))
valordahora = float(input("Digite o valor da hora: "))

salariobruto = horastrabalhadas * valordahora

salariofinal = salariobruto - ((2 / 100)* salariobruto)

print(f"O salário final de {nome} é de {salariofinal} reais")