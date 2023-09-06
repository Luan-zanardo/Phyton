opcao = "S"

while (opcao == "S"):
	a = int(input("Informe nr habitantes pais A:")) #total habitantes
	taxaa = float(input("Informe taxa crescimento pais A:"))

	b = int(input("Informe nr habitantes pais B:"))
	taxab = float(input("Informe taxa crescimento pais A:"))
	anos = 0  # calcular

	while a <= b:
		a += a * taxaa    #CALC. taxa crescimento
		b += b * taxab
		anos += 1

	print ("Populacao do pais A ultrapassa ou iguala ao pais  B em ", anos," anos")
	print("Habitantes País A: ",a)
	print("Habitantes País B: ",b)

	opcao = input("Deseja continuar S ou N?")
	if opcao == "N":
		break