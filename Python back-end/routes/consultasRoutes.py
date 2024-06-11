from controllers.consultasController import consultasController

def consultas(app):
    app.route('/consultas', methods=['POST', 'GET', 'PUT', 'DELETE'])(consultasController)