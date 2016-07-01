from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_wtf.csrf import CsrfProtect
from flask_admin import Admin
from sqlalchemy_searchable import make_searchable


app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
make_searchable()

CsrfProtect(app)
bcrypt = Bcrypt(app)

import aalert.manage
import aalert.views

from aalert.models import User

#login configuration
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id==userid).first()

