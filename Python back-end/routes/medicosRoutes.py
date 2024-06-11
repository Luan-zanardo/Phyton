from controllers.medicosController import medicosController

def medicos(app):
    app.route('/medicos', methods=['POST', 'GET', 'PUT', 'DELETE'])(medicosController)