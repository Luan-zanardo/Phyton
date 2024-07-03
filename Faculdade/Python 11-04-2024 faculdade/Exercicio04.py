letra = input("Digite uma letra: ").upper()

if letra in 'AEIOU':
    print(f"{letra} é uma vogal")
else:
     print(f"{letra} é uma consoante")