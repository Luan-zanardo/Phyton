from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class medicos(db.Model):

    def to_dict(self):
        return{
            'codusuario': self.codusuario,
            'nome':self.nome,
            'especializacao':self.especializacao,
            'afiliacao hospitalar':self.afiliacaohospitalar
        }
    
    codigo = db.Column(db.Integer, primary_key=True)
    codusuario = db.Column(ForeignKey('usuarios.codigo'))
    nome = db.Column(db.String(50))
    especializacao = db.Column(db.String(50))
    afiliacaohospitalar = db.Column(db.String(50))

    usuario = relationship('usuarios', backref='medicos')

    def __init__(self,codusuario, nome,especializacao, afiliacaohospitalar):
        self.codusuario = codusuario
        self.nome = nome
        self.especializacao = especializacao
        self.afiliacaohospitalar = afiliacaohospitalar