preco = float(input("Digite preço: "))

desconto = preco * 0.2
precofinal = preco - desconto

print(f"Preço original: R$ {preco:.2f}")
print(f"Você ganhou R$ {desconto:.2f} de desconto")
print(f"Preço com desconto: R$ {precofinal:.2f}")