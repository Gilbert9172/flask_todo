import os

BASE_DIR = os.path.dirname(__file__)


db = {
    'user'     : 'root',		
    'password' : 'Wjdrlfwns1!',	
    'host'     : 'localhost',	
    'port'     : 3306,			
    'database' : 'gilbert_db'		
}

#-- sqlite 연동 
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

#-- MySQL연동
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False

#-- Flask-WTF를 사용하기 위해서 SECRET_KEY설정
SECRET_KEY = 'dev'

