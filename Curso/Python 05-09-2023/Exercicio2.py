"""Faça um script que leia um número e mostre o seu dobro, seu triplo e a sua raiz quadrada"""

a = int(input("Digite um valor: "))

dobro = a * 2
triplo = a * 3
raiz = a ** (1/2)

print(f"o dobro de {a} é {dobro}" )
print(f"o triplo de {a} é {triplo}" )
print(f"a raiz de {a} é {round(raiz, 2)}" )