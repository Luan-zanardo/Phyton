def verificar_numero(numero, vetor):
    if numero in vetor:
        return True
    return False

vetor = []

while len(vetor) < 10:
    numero = int(input("Digite um número: "))

    if verificar_numero(numero, vetor):
        print("Número já digitado. Digite outro número.")
    else:
        vetor.append(numero)

print("Vetor final:", vetor)