
import jwt
from datetime import datetime,timedelta
from calendar import timegm

from werkzeug import generate_password_hash,check_password_hash
from flask import current_app

from rmon.common.errors import InvalidTokenError,AuthenticationError
from rmon.extensions import db

from .base import BaseModel


class User(BaseModel):

    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    wx_id=db.Column(db.String(32),unique=True)
    name=db.Column(db.String(64),unique=True)
    email=db.Column(db.String(64),unique=True)
    _password=db.Column(db.String(128))
    is_admin=db.Column(db.Boolean,default=False)
    login_at=db.Column(db.DateTime)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,password):
        sefl._password=generate_password_hash(passwd)

    def verify_password(self,password):
        pass

    @classmethod
    def authenticate(cls,identifier,password):
        user=cls.query.filter(db.or_(cls.name==identifier,
                                     cls.email==idenfifier)).first()
        if user is None or not user.verify_password(password):
            raise AuthenticationError(403,'authentication failed')
        return user

    def generate_token(self):
        exp=datetime.utcnow()+timedelta(days=1)
        refresh_exp=timegm((exp+timedelta(seconds=60*10)).utctimeuple())

        payload={
            'uid':self.id,
            'is_admin':self.is_admin,
            'exp':exp,
            'refresh_exp':refresh_exp
                }
        return jwt.encode(payload,current_app.secret_key,
                          algorithm='HS512').decode('utf-8')
    @classmethod
    def verify_token(cls,token,verify_exp=True):
        pass

    @classmethod
    def create_administrator(cls):
        pass

    @classmethod
    def wx_id_user(cls,wx_id):
        return cls.query.filter_by(wx_id=wx_id).first()

    
