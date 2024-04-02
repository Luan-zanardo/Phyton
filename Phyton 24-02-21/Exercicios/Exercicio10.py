'''10) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. 
Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também 
testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão 
escrever a mensagem 'Saldo Negativo'.'''

conta = int(input("Digite numero da conta: "))
saldo = int(input("Digite saldo: "))
debito = int(input("Digite débito: "))
credito = int(input("Digite crédito: "))

saldoatual = saldo - debito + credito

if(saldoatual >= 0):
    print(f"saldo postivo: {saldoatual}")
else:
    print(f"saldo negativo: {saldoatual}")