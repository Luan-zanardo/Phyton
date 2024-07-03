torque = float(input("Digite valor do torque em Nm: "))
torqueRecomendado = float(input("Digite valor do torque de aperto recomendado em Nm: "))

acima = torqueRecomendado + (torqueRecomendado * (10/100))
abaixo = torqueRecomendado - (torqueRecomendado * (10/100))

if(torque < acima and torque > abaixo):
    print("O parafuso está apertado corretamente.")
else:
    print("O parafuso não está apertado corretamente.")