a = 80000   #total habitantes
b = 200000
anos = 0   #calcular

while a <= b:
	a += a * 0.03    #taxa crescimento
	b += b * 0.015
	anos += 1

print ("Populacao do pais A ultrapassa ou iguala ao pais  B em ", anos," anos")
print("Habitantes País A: ",a)
print("Habitantes País B: ",b)
