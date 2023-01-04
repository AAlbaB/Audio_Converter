from flask import send_file
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import db, User, Task

class VistaFiles(Resource):
    @jwt_required()
    def get(self, fileName):
        # Retorna el archivo convertido
        # Endpoint http://localhost:5000/api/files/fileName

        current_user = get_jwt_identity()
        user = User.query.get(current_user)
        user_id = user.id

        if db.session.query(Task.query.filter(Task.fileName.contains(fileName),
            Task.user == user_id).exists()).scalar():

            task_consulta = Task.query.filter(Task.fileName.contains(fileName),
            Task.user == user_id).order_by(Task.id.desc()).first()

            if task_consulta.status == 'processed':
                try:
                    return send_file(task_consulta.pathConvertido)
                except Exception as e:
                    return str(e)
            
            else:
                try:
                    return send_file(task_consulta.pathOriginal)
                except Exception as e:
                    return str(e)
        
        else:
            return {'mensaje':'El archivo no existe para el usuario'}, 400