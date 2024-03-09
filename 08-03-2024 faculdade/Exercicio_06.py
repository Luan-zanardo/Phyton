dinheiro = float(input("Quantidade de dinheiro: "))

litros = dinheiro / 4.95
km = litros * 20

print(f"Com R$ {dinheiro:.2f}, você consegue comprar {litros:.2f} litros de combustível")
print(f"Com {litros:.2f} litros de combustível você consegue rodar {km:.2f} km")