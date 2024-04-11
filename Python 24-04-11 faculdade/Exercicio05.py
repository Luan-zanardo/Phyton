nota1 = float(input("Digite nota 1: "))
nota2 = float(input("Digite nota 2: "))
nota3 = float(input("Digite nota 3: "))

media = (nota1 + nota2 + nota3) / 3
media = round(media, 2)

if(media >= 7):
    print(f"Nota: {media}, Parabéns! Sua média é alta.")
elif(media >= 5 and media < 7):
    print(f"Nota: {media}, Sua média é razoável.")
elif(media < 5):
    print(f"Nota: {media}, Sua média é baixa. É uma boa oportunidade para melhorar.")