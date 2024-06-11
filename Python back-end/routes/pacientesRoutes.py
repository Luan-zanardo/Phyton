from controllers.pacientesController import pacientesController

def pacientes(app):
    app.route('/pacientes', methods=['POST', 'GET', 'PUT', 'DELETE'])(pacientesController)