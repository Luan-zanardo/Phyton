from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def verificar_aposentadoria(idade, anos_trabalhados):
    if idade >= 65 or anos_trabalhados >= 30 or (idade >= 60 and anos_trabalhados >= 25):
        return True
    else:
        return False

def main():
    codigo = int(input("Digite o número do empregado (código): "))
    ano_nascimento = int(input("Digite o ano de nascimento do empregado: "))
    ano_ingresso = int(input("Digite o ano de ingresso na empresa: "))

    idade = calcular_idade(ano_nascimento)
    anos_trabalhados = datetime.now().year - ano_ingresso

    print(f"Idade do empregado: {idade} anos")
    print(f"Tempo de trabalho: {anos_trabalhados} anos")

    if verificar_aposentadoria(idade, anos_trabalhados):
        print("Requerer aposentadoria")
    else:
        print("Não requerer aposentadoria")

if __name__ == "__main__":
    main()