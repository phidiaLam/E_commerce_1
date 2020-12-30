'''
Autor: Wentao Lin
Description: To create the database
Date: 2020-12-26 12:18:25
LastEditTime: 2020-12-26 12:18:35
LastEditors: Wentao Lin
'''

from config import SQLALCHEMY_DATABASE_URI
from app import db
import os.path
db.create_all()
