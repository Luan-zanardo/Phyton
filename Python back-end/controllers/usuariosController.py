from flask import request, render_template
from database.db import db
from models.usuarios import usuarios

def usuariosController():
    if request.method == 'POST':
        try:
            data = request.get_json()
            user = usuarios(data['nome'], data['email'], data['senha'], data['papel'])
            db.session.add(user)
            db.session.commit()
            return 'Usuário criado com sucesso', 200
        except:
            return 'O usuário não foi criado', 405
        
    elif request.method == 'GET':
        try:
            data = usuarios.query.all()
            new = {'usuarios': [cargo.to_dict() for cargo in data]}
            return new, 200
        except Exception as e:
            return 'Não foi possível buscar usuários', 405
        
    elif request.method == 'PUT':
         try:
              data = request.get_json()
              put_usuario_id = data['codigo']
              put_usuario = usuarios.query.get(put_usuario_id)
              if put_usuario is None:
                   return {'error': 'usuário não encontrado'}, 404
              put_usuario.nome = data.get('nome', put_usuario.nome)
              put_usuario.email = data.get('email', put_usuario.email)
              put_usuario.senha = data.get('senha', put_usuario.senha)
              put_usuario.papel = data.get('papel', put_usuario.papel)
              db.session.commit()
              return 'usuário atualizado com sucesso', 200
         except Exception as e:
              return {'error': 'Erro ao atualizar usuário. Erro {}'.format(e)}, 400
         
    elif request.method == 'DELETE':
        try:
            data = request.get_json()
            usuario_id = data['codigo']
            usuario = usuarios.query.get(usuario_id)
            if usuario:
                db.session.delete(usuario)
                db.session.commit()
                return 'usuário excluído com sucesso', 200
            else:
                return {'error': 'usuário não encontrado'}, 404
        except Exception as e:
            return {'error': 'Erro ao excluir usuário. Erro {}'.format(e)}, 400