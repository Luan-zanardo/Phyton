import os

clientesList = []
cardapioList = []

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def MostrarCardapio():
    if cardapioList:
            print("--------CARDÁPIO----------")
            cardapioList.sort(key=lambda item: item['codProd'])
            for item in cardapioList:
                print(f"{item['codProd']} | {item['nomeProd']} | {item['precoProd']} R$")
def Cardapio():
    while True:
        MostrarCardapio()
        print("--------OPÇÕES------------")
        op = int(input("1 - Adicionar\n"
                    "2 - Editar\n"
                    "3 - Excluir\n"
                    "4 - Voltar\n"))
        if(op == 1):
            limpar()
            MostrarCardapio()
            print("--------ADICIONAR ITEM--------")
            codProd = int(input("Código: "))
            nomeProd = input("Nome: ")
            precoProd = float(input("Preço: "))
            CardapioAdd(codProd, nomeProd, precoProd)
            limpar()
        elif(op == 2):
            limpar()
            MostrarCardapio()
            print("---------EDITAR ITEM----------")
            codProd = int(input("Código: "))
            CardapioEditar(codProd)
            limpar()
        elif(op == 3):
            limpar()
            MostrarCardapio()
            print("---------EXCLUIR ITEM---------")
            codProd = int(input("Código: "))
            CardapioExcluir(codProd)
            limpar()
        elif(op == 4):
            limpar()
            Inicio()
    
def CardapioAdd(codProd, nomeProd, precoProd):
    item = {
        'codProd': codProd,
        'nomeProd': nomeProd,
        'precoProd': precoProd
    }
    cardapioList.append(item)

def CardapioEditar(codProd):
    for item in cardapioList:
        if item['codProd'] == codProd:
            nomeProd = input(f"Nome do produto ({item['nomeProd']}): ")
            precoProd = input(f"Preço do produto ({item['precoProd']}): ")
            if nomeProd:
                item['nomeProd'] = nomeProd
            if precoProd:
                item['precoProd'] = float(precoProd)
def CardapioExcluir(codProd):
    for item in cardapioList:
        if item['codProd'] == codProd:
            cardapioList.remove(item)

def MostartClientes():
    if clientesList:
            print("--------COMANDA----------")
            clientesList.sort(key=lambda cliente: cliente['cod'])
            for cliente in clientesList:
                print(f"Código: {cliente['cod']} | Nome: {cliente['nome']} | Total: {cliente['total']}")

def Comanda():
    while True:
        MostartClientes()
        print("---------OPÇÕES-----------")
        op = int(input("1 - Adicionar\n"
                        "2 - Editar\n"
                        "3 - Excluir\n"
                        "4 - Abrir\n"
                        "5 - Voltar\n"))
        if(op == 1):
            limpar()
            MostartClientes()
            print("--------ADICIONAR CLIENTE--------")
            codCliente = int(input("Código: "))
            nomeCliente = input("Nome: ")
            ClienteAdd(codCliente, nomeCliente)
            limpar()
        elif(op == 2):
            limpar()
            MostartClientes()
            print("---------EDITAR CLIENTE----------")
            codCliente = int(input("Código: "))
            ClienteEditar(codCliente)
            limpar()
        elif(op == 3):
            limpar()
            MostartClientes()
            print("---------EXCLUIR CLIENTE---------")
            codCliente = int(input("Código: "))
            ClienteExcluir(codCliente)
            limpar()
        elif(op == 4):
            limpar()
            MostartClientes()
            print("--------ABRIR COMANDA------------")
            cod = int(input('Código: '))
            limpar()
            AbrirComanda(cod)
        elif(op==5):
            limpar()
            Inicio()

def ClienteAdd(codCliente, nomeCliente):
    comanda = []
    total = 0
    cliente = {
        'cod': codCliente,
        'nome': nomeCliente,
        'comanda': comanda,
        'total' : total
    }
    clientesList.append(cliente)

def ClienteEditar(codCliente):
    for cliente in clientesList:
        if cliente['cod'] == codCliente:
            nome= input(f"Nome do cliente ({cliente['nome']}): ")
            if nome:
                cliente['nome'] = nome

def ClienteExcluir(codCliente):
    for cliente in clientesList:
        if cliente['cod'] == codCliente:
            clientesList.remove(cliente)

def MostrarComanda(cliente):
        print("----------COMANDA---------")
        print(f"> Código: {cliente['cod']}")
        print(f"> Nome: {cliente['nome']}")
        print(f"> Total: {cliente['total']}\n")

        for item in cliente['comanda']:
            print(f"Código: {item['codProd']} | {item['quantidadeProd']}x | {item['nomeProd']} | {item['precoProd']} R$")

def AbrirComanda(cod):
    for cliente in clientesList:
        if cliente['cod'] == cod:
            while True:
                MostrarComanda(cliente)
                print("---------OPÇÕES-----------")
                op = int(input("1 - Adicionar\n"
                                "2 - Editar\n"
                                "3 - Excluir\n"
                                "4 - Voltar\n"))
                if op == 1:
                    limpar()
                    MostrarCardapio()
                    print("----------ADICIONAR ITEM---------")
                    ComandaAdd(cliente)
                    limpar()
                elif op == 2:
                    limpar()
                    MostrarComanda(cliente)
                    print("--------EDITAR ITEM------------")
                    codProd = int(input("Código: "))
                    ComandaEditar(cliente, codProd)
                    limpar()
                elif op == 3:
                    limpar()
                    MostrarComanda(cliente)
                    print("--------EXCLUIR ITEM------------")
                    codProd = int(input("Código: "))
                    ComandaExcluir(cliente, codProd)
                    limpar()
                elif op == 4:
                    limpar()
                    Comanda()

def ComandaAdd(cliente):
    codProd = int(input("Código: "))
    quantidadeProd = int(input("Quantidade: "))

    for item in cardapioList:
        if item['codProd'] == codProd:
            itemComanda = {
                'codProd': item['codProd'],
                'quantidadeProd': quantidadeProd,
                'nomeProd': item['nomeProd'],
                'precoProd': item['precoProd'],
            }
            cliente['comanda'].append(itemComanda)
            cliente['total'] += quantidadeProd * item['precoProd']

def ComandaEditar(cliente, codProd):
    for item in cliente['comanda']:
        if item['codProd'] == codProd:
            cliente['total'] -= item['quantidadeProd'] * item['precoProd']
            quantProd = int(input(f"Quantidade produto ({item['quantidadeProd']}): "))
            if quantProd:
                item['quantidadeProd'] = quantProd
                cliente['total'] += quantProd * item['precoProd']

def ComandaExcluir(cliente, codProd):
    for item in cliente['comanda']:
        if item['codProd'] == codProd:
            cliente['comanda'].remove(item)
            cliente['total'] -= item['quantidadeProd'] * item['precoProd']

def Inicio():
    while True:
        print("--------MENU----------")
        op = int(input("1 - Cardapio\n"
                    "2 - Comandas\n"
                    "3 - Sair\n"))
        if(op == 1):
            limpar()
            Cardapio()
        elif(op == 2):
            limpar()
            Comanda()
        elif(op == 3):
            break
        
Inicio()