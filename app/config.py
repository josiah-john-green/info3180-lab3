import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv()

class Config(object): 

    """Base Config Object""" 

    DEBUG = True 
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y') 
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'sandbox.smtp.mailtrap.io') 
    MAIL_PORT = os.environ.get('MAIL_PORT', '25') 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'f0626403b8b10e') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'd488b4cb5e807a')
