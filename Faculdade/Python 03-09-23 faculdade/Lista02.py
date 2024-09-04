class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = []
    
    def filaVazia(self):
        return len(self.fila) == 0
    
    def filaCheia(self):
        return len(self.fila) == self.tamanho
    
    def enfileirar(self, valor):
        if self.filaCheia():
            raise Exception("A fila está cheia.")
        self.fila.append(valor)
    
    def desenfileirar(self):
        if self.filaVazia():
            raise Exception("A fila está vazia.")
        return self.fila.pop(0)
    
    def primeiro(self):
        if self.filaVazia():
            raise Exception("A fila está vazia.")
        return self.fila[0]

minha_fila = Fila(len("Luan"))

# b.
for char in "Luan":
    minha_fila.enfileirar(char)

print("Fila após enfileiramento:", minha_fila.fila)

# c
try:
    minha_fila.enfileirar('X')
except Exception as e:
    print(e)

# d
print("Primeiro elemento da fila:", minha_fila.primeiro())

# e
for _ in range(3):
    minha_fila.desenfileirar()

print("Fila após desenfileirar 3 vezes:", minha_fila.fila)
print("Primeiro elemento da fila após desenfileirar 3 vezes:", minha_fila.primeiro())
