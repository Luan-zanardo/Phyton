op = input("Digite:\n"
           "(M) -> para masculino\n"
           "(F) -> para feminino\n").upper()

if(op == "M"):
    print("Sexo masculino")
elif(op == "F"):
    print("Sexo feminino")
else:
    print("Sexo inválido")