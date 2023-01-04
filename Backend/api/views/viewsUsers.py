import os
from celery import Celery
from datetime import datetime
from dotenv import load_dotenv
from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required
from ..models import db, User, UserSchema
from ..utils import validate_password

load_dotenv()
celery_app = Celery('__name__', broker = os.getenv('BROKER_URL'))

@celery_app.task(name = 'registrar_login')
def registrar_log(*args):
    pass

user_schema = UserSchema()

class VistaUsers(Resource):

    def get(self):
        # Retorna todos los usuarios registrados
        # Endpoint http://localhost:5000/api/users

        return [user_schema.dump(user) for user in User.query.all()]

class VistaUser(Resource):
    
    @jwt_required()
    def get(self, id_user):
        # Retorna un usuario por su id
        # Endpoint http://localhost:5000/api/users/id_user

        return user_schema.dump(User.query.get_or_404(id_user))

    @jwt_required()
    def put(self, id_user):
        # Actualiza la contraseña de un usuario por su id
        # Endpoint http://localhost:5000/api/users/id_user

        user = User.query.get_or_404(id_user)
        user.password = request.json.get('password', user.password)
        db.session.commit()
        return user_schema.dump(user)

    @jwt_required()
    def delete(self, id_user):
        # Elimina un usuario por su id
        # Endpoint http://localhost:5000/api/users/id_user

        user = User.query.get_or_404(id_user)
        db.session.delete(user)
        db.session.commit()
        return 'Operacion Exitosa', 204

class VistaSignUp(Resource):

    def post(self):
        # Crea un usuario en la aplicacion
        # Endpoint http://localhost:5000/api/auth/signup

        user_username = User.query.filter(User.username == request.json['username']).first()
        user_email = User.query.filter(User.email == request.json['email']).first()

        #TODO: Encriptar contraseñas
        first_pass = request.json['password']
        second_pass = request.json['password_again']

        if user_username is not None:
            return {'mensaje': 'Nombre de usuario ya existe, por favor iniciar sesión'}, 203

        if user_email is not None:
            return {'mensaje': 'Correo electronico ya existe, por favor iniciar sesión'}, 203

        if first_pass != second_pass:
            return {'mensaje': 'Contaseñas no coinciden, por favor vuelve a intentar'}, 401

        if validate_password(first_pass) == False:
            return {'mensaje': 'La contraseña debe tener entre 8 y 24 caracteres, letras mayusculas, minisculas y numeros'}, 400

        try:
            new_user = User(username = request.json['username'], 
                            password = request.json['password'], 
                            email =request.json['email'])
                        
            db.session.add(new_user)
            db.session.commit()

            return {'mensaje': 'Usuario creado exitosamente', 
                    'id': new_user.id, 'usuario': new_user.username, 
                    'email': new_user.email}, 200

        except:
                return {'mensaje': 'A ocurrido un error, por favor vuelve a intentar'}, 503
                               
class VistaLogIn(Resource):

    def post(self):
        # Loguea un usuario en la aplicacion
        # Endpoint http://localhost:5000/api/auth/login

        try:
            usuario = User.query.filter(User.username == request.json['username'],
                                        User.password == request.json['password']).first()

            if usuario:
                args = (request.json['username'], datetime.utcnow())
                registrar_log.apply_async(args = args)
                token_de_acceso = create_access_token(identity = usuario.id)
                return {'mensaje':'Inicio de sesión exitoso', 'token': token_de_acceso}, 200
                            
            else:
                return {'mensaje':'Nombre de usuario o contraseña incorrectos'}, 401
            
        except Exception as e:
            return {'mensaje': 'A ocurrido un error, por favor vuelve a intentar', 'error': str(e)}, 503