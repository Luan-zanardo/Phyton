preco = float(input("Digite preço: "))
desconto = (float(input("Digite quantos % de desconto você pretende dar: ")) / 100) * preco

precofinal = preco - desconto

print(f"Preço original: R$ {preco:.2f}")
print(f"Você ganhou R$ {desconto:.2f} de desconto")
print(f"Preço com desconto: R$ {precofinal:.2f}")