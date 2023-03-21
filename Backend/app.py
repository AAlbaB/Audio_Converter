from Backend import create_app
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from Backend.api.models import db
from Backend.api.views import VistaUser, VistaUsers, VistaSignUp, VistaLogIn, \
    VistaTask, VistaTasksUser, VistaFiles

app = create_app('default')
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
api.add_resource(VistaFiles, '/api/files/<string:taskName>')

jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)
