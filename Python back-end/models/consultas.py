from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class consultas(db.Model):

    def to_dict(self):
        return{
            'codpaciente': self.codpaciente,
            'codmedico': self.codmedico,
            'horariodata':self.horariodata,
            'status':self.status,
            'descricao':self.descricao
        }
    
    codigo = db.Column(db.Integer, primary_key=True)
    codpaciente = db.Column(ForeignKey('pacientes.codigo'))
    codmedico = db.Column(ForeignKey('medicos.codigo'))
    horariodata = db.Column(db.Date)
    status = db.Column(db.String(50))
    descricao = db.Column(db.String(200))

    paciente = relationship('pacientes', backref='consultas')
    medico = relationship('medicos', backref='consultas')

    def __init__(self,codpaciente, codmedico, horariodata, status, descricao):
        self.codpaciente = codpaciente
        self.codmedico = codmedico
        self.horariodata = horariodata
        self.status = status
        self.descricao = descricao
