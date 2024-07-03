'''6) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem 
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e 
escreva o custo total da compra.'''

macas = int(input("Maças compradas: "))
preco = 0

if(macas >= 12):
    preco = macas * 1
elif(macas < 12):
    preco = macas * 1.30

print(f"O valor final para a compra de {macas} maças fica {preco} reais")