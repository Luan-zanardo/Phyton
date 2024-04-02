'''3) O custo de um carro novo ao consumidor é a soma do custo de fábrica 
com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). 
Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever 
um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.'''

custo = int(input("preço carro: "))

def percentual(porcentagem):
    perc = ((custo * porcentagem) / 100)
    return perc

distribuidor = percentual(28)
impostos = percentual(45)
custofabrica = custo - (distribuidor + impostos)

print(f"Preço do percentual de 28% do distribuidor: {distribuidor}")
print(f"Preço do percentual de 45% dos impostos : {impostos}")
print(f"Custo de fabrica: {custofabrica}")