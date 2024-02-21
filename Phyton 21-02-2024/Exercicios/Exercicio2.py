'''2) Escreva um algoritmo para ler o número total de eleitores de um município, 
o número de votos brancos, nulos e válidos. Calcular e escrever o percentual 
que cada um representa em relação ao total de eleitores. '''

brancos = int(input("Votos brancos: "))
nulos = int(input("Votos nulos: "))
validos = int(input("Votos válidos: "))

total = brancos + nulos + validos

def percentual(a): 
    perc = ((100 * a) / total)
    return perc

print(f"O total de votos é: {total}")
print(f"O percentual de votos brancos é: {percentual(brancos)}")
print(f"O percentual de votos nulos é: {percentual(nulos)}")
print(f"O percentual de votos validos é: {percentual(validos)}")