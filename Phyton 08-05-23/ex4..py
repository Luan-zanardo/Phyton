maiorindice = 0  #usar para comparar os indices acidentes
menorindice = 0
cidadeMaisAcidentes = ""    #usar para armazenar as cidades
cidadeMenosAcidentes = ""
totalveiculos = 0
totalacidentes = 0
nrcidademenor2000 = 0
contador = 1
for contador in range(5):
    cidade    = input("Digite nome cidade: ")
    veiculos  = int(input("Informe nr veiculos passeio: "))
    acidentes = int(input("Informe nr acidentes com vítimas: "))
    if (acidentes > maiorindice):
        maiorindice = acidentes
        cidadeMaisAcidentes = cidade
    if (acidentes < menorindice):
        menorindice = acidentes
        cidadeMenosAcidentes = cidade
    totalveiculos = totalveiculos + veiculos
    if (veiculos < 2000):
        totalacidentes = totalacidentes + acidentes
        nrcidademenor2000 = nrcidademenor2000 + 1

print ("Cidade Mais Acidentes      : ",cidadeMaisAcidentes)
print ("Total de acidentes (maior) : ",maiorindice)
print ("Cidade Menos Acidentes     : ",cidadeMenosAcidentes)
print ("Total de acidentes (menor( : ",menorindice)
mediaveiculos = totalveiculos / 5
mediaacidentes = totalacidentes / nrcidademenor2000
print ("Media de veiculos : ",mediaveiculos)
print ("Media de acidentes cidades < 2000 veiculos : ",mediaacidentes)