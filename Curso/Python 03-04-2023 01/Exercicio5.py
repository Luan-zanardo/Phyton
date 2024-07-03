nome = input("Digite seu nome:")
sexo= input("Digite seu sexo:")
altura= float(input("Digite sua altura:"))

if sexo == "m":
 pesoideal= (72.7 * altura) - 58
 print(nome, "seu peso ideal é:",pesoideal)

if sexo == "f":
    pesoideal= (62.1 * altura) - 44.7
    print (nome, "seu peso ideal é:",pesoideal)


