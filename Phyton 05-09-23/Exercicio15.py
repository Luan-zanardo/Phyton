"""Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem natela dizendo se está 
“quente”, “frio” ou “agradável”."""

temperatura = int(input("Digite a temperatura atual: "))

if(temperatura <= 15):
    print("Está Frio")
elif(temperatura > 15 and temperatura < 25):
    print("Está Agradavel")
elif(temperatura >= 25):
    print("Está Quente")