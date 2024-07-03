'''Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde h corresponde à altura):
• Homens: (72.7 ∗ h) − 58
• Mulheres: (62, 1 ∗ h) − 44, 7'''

h = float(input("Digite altura: "))
sexo = input("Digite (M) para masculino e (F) para femenino: ")

if(sexo == "M"):
    pesoideal = (72.7 * h) - 58
    print(f"Você é homem e seu peso ideal é {round(pesoideal, 2)} quilos")
elif(sexo == "F"):
   pesoideal = (62.1 * h) - 44.7
   print(f"Você é mulher e seu peso ideal é {round(pesoideal, 2)} quilos")