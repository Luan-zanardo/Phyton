frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

total_caracteres = len(frase)
total_letras = frase.count(letra)

print(f"Total de Letras encontradas na frase: {total_letras}")
print(f"Total de Caracteres na Frase: {total_caracteres}")