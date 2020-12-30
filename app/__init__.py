'''
Autor: Wentao Lin
Description: init the app 
Date: 2020-12-26 12:15:57
LastEditTime: 2020-12-26 20:46:53
LastEditors: Wentao Lin
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
# from wtforms.csrf import CSRFProtect

# csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_object('config')
# csrf.init_app(app)
db = SQLAlchemy(app)


admin = Admin(app,template_mode='bootstrap3')
migrate = Migrate(app,db,render_as_batch=True)
from app import views, models

