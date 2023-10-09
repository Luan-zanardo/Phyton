import random
palavraslista = ["cabelereiro", "caminhão", "cozinha", "toalha", "coliseu"]
escolhas = []

def pede_chute():
    print()
    print(f"letras que você ja escolheu: {escolhas}")
    chute = input("Escolha uma letra: ")
    escolhas.append(chute)
    return chute

def marca_chute(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print()
    print("  _______     ")
    print(" |/      |    ")
    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")
    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")
    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")
    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")
    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")
    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")
    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")
    print(" |            ")
    print("_|___         ")
    print()

palavra_secreta = random.choice(palavraslista)
letras_acertadas = ["_" for letra in palavra_secreta]
print(letras_acertadas)
enforcou = False
acertou = False
erros = 0
while(not enforcou and not acertou):
    chute = pede_chute()
    if(chute in palavra_secreta):
        marca_chute(chute, letras_acertadas, palavra_secreta)
    else:
        erros += 1
        desenha_forca(erros)
    enforcou = erros == 7
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)
if(acertou):
    print("Você ganhou!")
else:
    print("Você perdeu!")