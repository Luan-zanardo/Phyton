from controllers.prescricoesController import prescricoesController

def prescricoes(app):
    app.route('/prescricoes', methods=['POST', 'GET', 'PUT', 'DELETE'])(prescricoesController)