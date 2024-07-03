tensao = float(input("Digite valor de tensão em volts: "))
corrente = float(input("Digite valor da corrente em amperes: "))
resistencia = float(input("Digite valor da resistencia em ohms: "))

tensaoCalc = corrente * resistencia

if(tensao == tensaoCalc):
    print("O componente obedece à Lei de Ohm.")
else:
    print("O componente não obedece à Lei de Ohm.")