class Funcionario():
    def __init__(self, nome ,salario):
        self.nome = nome
        self.salario = salario

    def aumentoSalario(self, porcent):
        self.salario += self.salario*(porcent/100)
        print(self.salario)


nome = input("Digite nome: ")
salario = int(input("Digite salário: "))
porcent = int(input("Digite porcentagem: "))

funcionario = Funcionario(nome, salario)
print(funcionario.__dict__)