class Aluno:
    def __init__(self, nome ,curso, temposemdormir):
        self.nome = nome
        self.curso = curso
        self.temposemdormir = temposemdormir

    def estudar(self, horasestudo):
        self.temposemdormir += horasestudo
        print(self.temposemdormir)

    def dormir(self, horassono):
        self.temposemdormir -= horassono
        print(self.temposemdormir)

a = Aluno(nome="A", curso="TI", temposemdormir=12)
a.estudar(6)
a.dormir(8)