'''9) Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. 
Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 
5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.'''

salario = int(input("Salário fixo: "))
vendas = int(input("Valor das vendas efetuadas: "))
comissao = 0

if(vendas <= 1500):
    comissao = (vendas * 3) / 100
else:
    comissao = (vendas * 5) / 100

print(f"salário: {salario} reais,comissão: {comissao} reais, total: {salario + comissao} reais")