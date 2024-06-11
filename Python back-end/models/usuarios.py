from database.db import db

class usuarios(db.Model):

    def to_dict(self):
        return{
            'nome':self.nome,
            'email':self.email,
            'senha': self.senha,
            'papel': self.papel
        }
    
    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))
    senha = db.Column(db.String(50))
    papel = db.Column(db.String(50))

    def __init__(self,nome,email, senha, papel):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.papel = papel