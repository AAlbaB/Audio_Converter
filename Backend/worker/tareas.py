import os
import logging
from datetime import datetime
from celery import Celery
from pydub import AudioSegment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from api.models import Task, User, Login
from api.utils import send_email

PATH_LOGIN = os.getcwd() + '/logs/log_login.txt'
PATH_CONVERT = os.getcwd() + '/logs/log_convert.txt'

load_dotenv()
celery_app = Celery('__name__', broker = os.getenv('BROKER_URL'))
load_engine = create_engine(os.getenv('DATABASE_URL'))
write_bd = os.getenv('WRITE_LOGIN_BD')
Session = sessionmaker(bind = load_engine)
session = Session()

@celery_app.task(name = 'registrar_login')
def registrar_log(usuario, fecha):
    log_login.info('El usuario: {}, ha iniciado sesion'.format(usuario))
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
def convert_music(origin_path, dest_path, origin_format, new_format, name_file, task_id):

    new_task = session.query(Task).get(task_id)

    if origin_format == "mp3":
        sound = AudioSegment.from_mp3(origin_path)
        sound.export(dest_path, format = new_format)
        print ('\n-> El audio {}, se convirtio a : {}'.format(name_file, new_format))
        new_task.status = 'processed'
        session.commit()

    elif origin_format == "ogg":
        sound = AudioSegment.from_ogg(origin_path)
        sound.export(dest_path, format = new_format)
        print ('\n-> El audio {}, se convirtio a : {}'.format(name_file, new_format))
        new_task.status = 'processed'
        session.commit()

    elif origin_format == "wav":
        sound = AudioSegment.from_wav(origin_path)
        sound.export(dest_path, format = new_format)
        print ('\n-> El audio {}, se convirtio a : {}'.format(name_file, new_format))
        new_task.status = 'processed'
        session.commit()

    else:
        print ('No se proporciono una extension valida {}'.format(name_file))

    registrar_conversion(task_id, '-> El audio {}, se convirtio a : {}'.format(name_file, new_format),  
                            datetime.utcnow())
                            
    try: 
        user = session.query(User).get(new_task.user)
        send_email(user.email, new_task.fileName, new_task.newFormat)
        mensaje = '-> Se envio un email al usuario: {}'.format(user.username)
    except Exception as e:
        mensaje = '-> A ocurrido un error en el envio del email'

    registrar_conversion(task_id, mensaje, datetime.utcnow())

def registrar_conversion(id_task, mensaje, fecha):
    with open(PATH_CONVERT, 'a+') as file:
        file.write('Para la tarea con Id: {}, Se registro: {} - Con fecha: {}\n'.format(id_task, mensaje, fecha))

def setup_logger(name, log_file, level=logging.INFO):

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

log_login = setup_logger('log_login', PATH_LOGIN)

