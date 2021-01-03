'''
Autor: Wentao Lin
Description: 
Date: 2020-12-26 12:37:23
LastEditTime: 2021-01-03 19:27:26
LastEditors: Wentao Lin
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectMultipleField, SelectField, FileField
from wtforms.fields.html5 import DateField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class Signup(FlaskForm):
    username = StringField('username',  render_kw={'placeholder': 'Username',
                                                    'autofocus' : ''
                                                    },
                                        validators=[DataRequired(message='username cannot be empty')])
    password = PasswordField('password', render_kw={'placeholder': 'Password'},
                                        validators=[
                                                    DataRequired(message='password cannot be empty'),
                                                    Length(min=4, max=10, message='the length of password between 4 to 10')
                                                    ])
    re_password = PasswordField('re_password',  render_kw={'placeholder': 'Confirm Password'},
                                            validators=[
                                                    DataRequired(message='confirm password cannot be empty'),
                                                    EqualTo('password', message='two passwords do not match')
                                                    ])

class AddAddress(FlaskForm):
    house = StringField('detail', render_kw={'placeholder': 'House number',
                                                'autofocus' : ''
                                                },
                                    validators=[DataRequired()])
    street = StringField('street', render_kw={'placeholder': 'Street'},
                                    validators=[DataRequired()])
    city = StringField('city', render_kw={'placeholder': 'City'},
                                    validators=[DataRequired()])
    province = StringField('province', render_kw={'placeholder': 'Province'},
                                   )
    country = StringField('country', render_kw={'placeholder': 'Country'},
                                    validators=[DataRequired()])
    postcode = StringField('postcode', render_kw={'placeholder': 'Postcode'},
                                    validators=[DataRequired()])

class AddCommodity(FlaskForm):
    image = FileField('image', validators=[FileRequired(), 
                                            FileAllowed(['jpg','jpeg','png','gif'], message="select file in jpg, jepg, png and gif")])
    title = StringField('title', render_kw={'placeholder': 'Title'},
                                    validators=[DataRequired()])
    price = IntegerField('price', render_kw={'placeholder': 'Unite Price'},
                                   validators=[DataRequired("Place input numbers(Integer)")])
    number = IntegerField('number', render_kw={'placeholder': 'Number'},
                                    validators=[DataRequired("Place input numbers(Integer)")])
    classify = SelectField('classify', render_kw={'placeholder': 'Classify'},
                                    validators=[DataRequired()],
                                    choices = [('home appliances','home appliances'),('kitchen ware','kitchen ware'),('garden stuff','garden stuff'),('clothes','clothes'),('books','books'),('drinks','drinks'),('furniture','furniture'),('toys','toys')])          

class ChangePassword(FlaskForm):
    password = PasswordField('password', render_kw={'placeholder': 'Old Password'},
                                        validators=[
                                                    DataRequired(message='password cannot be empty'),
                                                    Length(min=4, max=10, message='the length of password between to in 4 to 10')
                                                    ])
    new_password = PasswordField('new_password', render_kw={'placeholder': 'New Password'},
                                        validators=[
                                                    DataRequired(message='password cannot be empty'),
                                                    Length(min=4, max=10, message='the length of password between to in 4 to 10')
                                                    ])
    re_password = PasswordField('re_password',  render_kw={'placeholder': 'Confirm Password'},
                                            validators=[
                                                    DataRequired(message='confirm password cannot be empty'),
                                                    EqualTo('new_password', message='two passwords do not match')
                                                    ])                          