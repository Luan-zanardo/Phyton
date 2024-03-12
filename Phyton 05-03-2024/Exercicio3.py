class Livros():
    def __init__(self, nome ,qtdPaginas, autor, preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco

    def getPreco(self):
        print(self.preco)
        
    def setPreco(self, preco):
        print("preço antigo: ", self.preco)
        self.preco = preco
        print("preco novo: ", self.preco)

a = Livros(nome="A", qtdPaginas=3, autor="fdssdf", preco=12)
a.getPreco()
a.setPreco(35)