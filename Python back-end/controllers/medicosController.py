from flask import request, render_template
from database.db import db
from models.medicos import medicos

def medicosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            pac = medicos(data['codusuario'], data['nome'], data['especializacao'], data['afiliacaohospitalar'])
            db.session.add(pac)
            db.session.commit()
            return 'Médico criado com sucesso', 200
        except:
            return 'O medico não foi criado', 405
        
    elif request.method == 'GET':
        try:
            data = medicos.query.all()
            new = {'medicos': [medico.to_dict() for medico in data]}
            return new, 200
        except Exception as e:
            return 'Não foi possível buscar médicos', 405
        
    elif request.method == 'PUT':
         try:
              data = request.get_json()
              put_medico_id = data['codigo']
              put_medico = medicos.query.get(put_medico_id)
              if put_medico is None:
                   return {'error': 'Médico não encontrado'}, 404
              put_medico.codusuario = data.get('codusuario', put_medico.codusuario)
              put_medico.nome = data.get('nome', put_medico.nome)
              put_medico.especializacao = data.get('especializacao', put_medico.especializacao)
              put_medico.afiliacaohospitalar = data.get('afiliacaohospitalar', put_medico.afiliacaohospitalar)
              db.session.commit()
              return 'Médico atualizado com sucesso', 200
         except Exception as e:
              return {'error': 'Erro ao atualizar médico. Erro {}'.format(e)}, 400
         
    elif request.method == 'DELETE':
        try:
            data = request.get_json()
            medico_id = data['codigo']
            medico = medicos.query.get(medico_id)
            if medico:
                db.session.delete(medico)
                db.session.commit()
                return 'Médico excluído com sucesso', 200
            else:
                return {'error': 'Médico não encontrado'}, 404
        except Exception as e:
            return {'error': 'Erro ao excluir médico. Erro {}'.format(e)}, 400