import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv 
from api.modelos import db
from api.vistas import VistaUser, VistaUsers, VistaSignUp, VistaLogIn, \
                        VistaTask, VistaTasksUser, VistaFiles

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True  
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors = CORS(app)

api = Api(app)
api.add_resource(VistaUsers, '/api/users')
api.add_resource(VistaUser, '/api/users/<int:id_user>')
api.add_resource(VistaSignUp, '/api/auth/signup')
api.add_resource(VistaLogIn, '/api/auth/login')
api.add_resource(VistaTasksUser, '/api/tasks')
api.add_resource(VistaTask, '/api/tasks/<int:id_task>')
api.add_resource(VistaFiles, '/api/files/<string:fileName>')

jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')