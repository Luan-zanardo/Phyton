from routes.consultasRoutes import consultas
from routes.medicosRoutes import medicos
from routes.pacientesRoutes import pacientes
from routes.prescricoesRoutes import prescricoes
from routes.usuariosRoutes import usuarios

def default_routes(app):
    consultas(app)
    medicos(app)
    pacientes(app)
    prescricoes(app)
    usuarios(app)