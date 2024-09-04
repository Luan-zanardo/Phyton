class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.pilha = []
    
    def pilhaVazia(self):
        return len(self.pilha) == 0
    
    def pilhaCheia(self):
        return len(self.pilha) == self.tamanho
    
    def empilhar(self, valor):
        if self.pilhaCheia():
            raise Exception("A pilha está cheia.")
        self.pilha.append(valor)
    
    def desempilhar(self):
        if self.pilhaVazia():
            raise Exception("A pilha está vazia.")
        return self.pilha.pop()
    
    def topo(self):
        if self.pilhaVazia():
            raise Exception("A pilha está vazia.")
        return self.pilha[-1]

minha_pilha = Pilha(10)

# b
for char in "Luan":
    minha_pilha.empilhar(char)

print("Pilha após empilhamento:", minha_pilha.pilha)

# c
try:
    for i in range(6):
        minha_pilha.empilhar(str(i))
    print("Pilha após encher:", minha_pilha.pilha)
except Exception as e:
    print(e)

# d
print("Elemento no topo da pilha:", minha_pilha.topo())

# e
for _ in range(3):
    minha_pilha.desempilhar()

print("Pilha após desempilhar 3 vezes:", minha_pilha.pilha)
print("Elemento no topo da pilha após desempilhar 3 vezes:", minha_pilha.topo())