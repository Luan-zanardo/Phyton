from flask import request, render_template
from database.db import db
from models.pacientes import pacientes

def pacientesController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            pac = pacientes(data['codusuario'], data['nome'], data['nascimento'], data['genero'], data['endereco'])
            db.session.add(pac)
            db.session.commit()
            return 'Paciente criado com sucesso', 200
        except:
            return 'O paciente não foi criado', 405
        
    elif request.method == 'GET':
        try:
            data = pacientes.query.all()
            new = {'pacientes': [paciente.to_dict() for paciente in data]}
            return new, 200
        except Exception as e:
            return 'Não foi possível buscar pacientes', 405
        
    elif request.method == 'PUT':
         try:
              data = request.get_json()
              put_paciente_id = data['codigo']
              put_paciente = pacientes.query.get(put_paciente_id)
              if put_paciente is None:
                   return {'error': 'Paciente não encontrado'}, 404
              put_paciente.codusuario = data.get('codusuario', put_paciente.codusuario)
              put_paciente.nome = data.get('nome', put_paciente.nome)
              put_paciente.nascimento = data.get('nascimento', put_paciente.nascimento)
              put_paciente.genero = data.get('genero', put_paciente.genero)
              put_paciente.endereco = data.get('endereco', put_paciente.endereco)
              db.session.commit()
              return 'Paciente atualizado com sucesso', 200
         except Exception as e:
              return {'error': 'Erro ao atualizar paciente. Erro {}'.format(e)}, 400
         
    elif request.method == 'DELETE':
        try:
            data = request.get_json()
            paciente_id = data['codigo']
            paciente = pacientes.query.get(paciente_id)
            if paciente:
                db.session.delete(paciente)
                db.session.commit()
                return 'Paciente excluído com sucesso', 200
            else:
                return {'error': 'Paciente não encontrado'}, 404
        except Exception as e:
            return {'error': 'Erro ao excluir paciente. Erro {}'.format(e)}, 400