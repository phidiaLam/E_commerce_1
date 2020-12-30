'''
Autor: Wentao Lin
Description: create a database models
Date: 2020-12-26 12:37:12
LastEditTime: 2020-12-30 15:10:20
LastEditors: Wentao Lin
'''

from app import db

shopping_cart = db.Table('shopping_cart', db.Model.metadata,
    db.Column('userId', db.Integer, db.ForeignKey('user.userId')),
    db.Column('goodsId', db.Integer, db.ForeignKey('goods.goodsId'))
)

shopping_order = db.Table('shopping_order', db.Model.metadata,
    db.Column('orderId', db.Integer, db.ForeignKey('order.orderId')),
    db.Column('goodsId', db.Integer, db.ForeignKey('goods.goodsId'))
)

class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    sell = db.Column(db.Boolean, default=False, nullable=False)
    good = db.relationship('Goods', backref='seller', lazy='dynamic')
    goods = db.relationship('Goods', secondary=shopping_cart)
    address = db.relationship('Address', backref='address owner', lazy='dynamic')
    order = db.relationship('Order', backref='order owner', lazy='dynamic')
    def __repr__(self):
        return self.username

class Goods(db.Model):
    goodsId = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(30), index=True)
    price = db.Column(db.Integer)
    number = db.Column(db.Integer)
    type = db.Column(db.String(20))
    # seller
    sell_goods = db.Column(db.Integer, db.ForeignKey('user.userId'))
    # Who buy this good
    users = db.relationship('User', secondary=shopping_cart)
    orders = db.relationship('Order', secondary=shopping_order)

class Address(db.Model):
    addressId = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(500), index=True)     
    user = db.Column(db.Integer, db.ForeignKey('user.userId'))

class Order(db.Model):
    orderId = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.userId'))
    goods = db.relationship('Goods', secondary=shopping_order)

