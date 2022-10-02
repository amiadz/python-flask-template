class Config(object):
    DEBUG = False
    SECRET_KEY = 'thisisasecretkey'

class DevConfig(Config):    
    DB_USERNAME = 'waiishzx'
    DB_PASSWORD = '2-XoFyDFOLOAolZFZBQVBQ1KE_931-mn'
    DB_HOST = 'drona.db.elephantsql.com'
    DB_DATABASE_NAME = 'waiishzx'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE_NAME}'

class LocalConfig(Config):    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
        
class ProdConfig(Config):    
    DB_USERNAME = ''
    DB_PASSWORD = ''
    DB_HOST = ''
    DB_DATABASE_NAME = ''
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE_NAME}'