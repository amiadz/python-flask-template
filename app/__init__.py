from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object('config.DevConfig')

from app.model import user
from app import views
from app import auth_views
from app import register_views
from app import health

User = user.User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))