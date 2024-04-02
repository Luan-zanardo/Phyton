nome = input("Digite usuário: ")
senha = input("Digite senha: ")

while (nome == senha): #repitir quando for igual
    print("Erro: senha invalida, deve ser diferente do usuário")
    senha = input("Digite uma nova senha: ")

print("Usuário e senha corretos!!!")