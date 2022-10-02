## Python Flask Template

### The stack

1. python - runtime
2. flask - Framework
3. SqlAlchemy - ORM
4. postgres - DB

---

### Configuration

In order to run the server, there is config.py in the repo.

#### config.py

```python
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
```

You can change the config in `app/__init__.py` by changing the following line to this:
```python
app.config.from_object('config.<desired config>')
```

You can also change the config parameters in `config.py` 

### How To Run

1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Then create local db: 
```
$ python
$ >>> from app.db_util import db
$ >>> db.create_all()
$ >>> exit()
```

6. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
