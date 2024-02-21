'''13) Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.'''

valor1 = int(input("Digite valor 1: "))
valor2 = int(input("Digite valor 2: "))
valor3 = int(input("Digite valor 3: "))

valoresordenados = sorted([valor1, valor2, valor3], reverse=True)
maiores = valoresordenados[0] + valoresordenados[1]
print(f"soma dos maiores valores: {maiores}")