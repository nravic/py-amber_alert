from random import SystemRandom
from datetime import datetime
from flask import Flask
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin
from flask_sqlalchemy import BaseQuery
from sqlalchemy_searchable import SearchQueryMixin
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import make_searchable

from aalert import db, bcrypt
#public information table

class InfoQuery(BaseQuery, SearchQueryMixin):
    pass

class Info(db.Model):
    query_class = InfoQuery
    __tablename__ = 'info'
    
    id = db.Column(db.Integer, primary_key=True, unique=True,
                   nullable=False, autoincrement=True)
    firstname = db.Column(db.Unicode(50))
    lastname = db.Column(db.Unicode(50))
    age = db.Column(db.Unicode(3))
    height = db.Column(db.Unicode(3))
    last_loc = db.Column(db.Unicode(180))
    missing_since = db.Column(db.Unicode(10))
    contact_info = db.Column(db.Unicode(15))
    home_address = db.Column(db.Unicode(80))
    search_vector = db.Column(TSVectorType('firstname', 'lastname', 'age', 'height', 'last_loc', 'missing_since',
                                           'contact_info', 'home_address'))

    def __init__(self, firstname=firstname, lastname=lastname, age=age, height=height, last_loc=last_loc,
                 missing_since=missing_since, contact_info=contact_info, home_address=home_address):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.height = height
        self.last_loc = last_loc
        self.missing_since = missing_since
        self.contact_info = contact_info
        self.home_address = home_address

        
    def __repr__(self):
        return '<Info %r>' % self.firstname
    


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    _password = db.Column(db.Binary(128))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

