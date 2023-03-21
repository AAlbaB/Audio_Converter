import os
import logging
from celery import Celery
from pydub import AudioSegment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from api.models import Task, User, Login
from api.utils import send_email

PATH_LOGIN = os.getcwd() + '/logs/log_login.log'
PATH_CONVERT = os.getcwd() + '/logs/log_convert.log'
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///audio_converter.db')

load_dotenv()
celery_app = Celery('__name__', broker = os.getenv('BROKER_URL'))
load_engine = create_engine(DATABASE_URL)
write_bd = os.getenv('WRITE_LOGIN_BD')
send_email = os.getenv('SEND_EMAIL')

Session = sessionmaker(bind = load_engine)
session = Session()

@celery_app.task(name = 'registrar_login')
def registrar_log(usuario, fecha):
    log_login.info('-> El usuario: {}, ha iniciado sesion'.format(usuario))
    print('-> El usuario: {}, ha iniciado sesión: {}'.format(usuario, fecha))

    if write_bd == 'True':
        try:
            new_login = Login(timeStamp = fecha, username = usuario, 
                            message = 'El usuario ha iniciado sesión exitosamente')

            session.add(new_login)
            session.commit()
            print('-> Registro agregado exitosamente en BD')
            
        except Exception as e:
            print('-> Ha ocurrido un error registrando el login en BD, {}'.format(e))

@celery_app.task(name = 'convert_music')
def convert_music(path_original, path_convertido, old_format, new_format,  task_name, task_id):

    try:
        new_task = session.query(Task).get(task_id)

        sound = AudioSegment.from_file(path_original, format = old_format)
        sound.export(path_convertido, format = new_format)
        new_task.status = 'processed'
        session.commit()

        print ('-> El audio {}, se convirtio a : {}'.format( task_name, new_format))
        mensaje = 'El audio {}, se convirtio a : {}'.format( task_name, new_format)

    except Exception as e:
        print ('\n-> A ocurrido un error convirtiendo el archivo ' + str(e))
        mensaje = 'A ocurrido un error convirtiendo el archivo ' + str(e)

    log_convert.info('Para la tarea con Id: {}, Se registro: {}'.format(task_id, mensaje))

    if new_task.status == 'processed' and send_email == 'True':                      
        try: 
            user = session.query(User).get(new_task.user)
            send_email(user.email, new_task.fileName, new_task.newFormat)
            mensaje = '-> Se envio un email al usuario: {}'.format(user.username)
        except Exception as e:
            mensaje = '-> A ocurrido un error en el envio del email {}'.format(e)

        log_convert.info('Para la tarea con Id: {}, Se registro: {}'.format(task_id, mensaje))

def setup_logger(name, log_file, level=logging.INFO):

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

log_login = setup_logger('log_login', PATH_LOGIN)
log_convert = setup_logger('log_convert', PATH_CONVERT)