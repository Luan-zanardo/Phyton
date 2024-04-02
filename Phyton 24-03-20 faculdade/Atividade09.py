'''Elabore um programa que leia uma frase, uma palavra antiga e uma palavra nova. O programa deve exibir uma string contendo a frase original e outra com a ocorrência da palavra antiga substituída pela palavra nova.​'''

frase = input("Digite uma frase: ")
palavraAntiga = input("Digite palavra antiga: ")
palavraNova = input("Digite palavra nova: ")
fraseNova = frase.replace(palavraAntiga, palavraNova)

print("Frase: {}".format(fraseNova))
