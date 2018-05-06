
"""
该模块实现了所有的 model 类以及相应的序列化类，
实现一个 Redis 服务器模型，对应到数据库中是一张表，用来存储 Redis 服务器信息。
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from redis import StrictRedis,RedisError
from rmon.commmon.rest import RestException


db=SQLAlchemy()

class Server(db.Model):
#Radis服务器模型
    __tablename__='radis_server'
#id值在数据库中唯一的确定一台Radis服务器
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    description=db.Column(db.String(512))
    host=db.Column(db.String(15))
    port=db.Column(db.Integer,default=6379)
    password=db.Column(db.String())
    updated_at=db.Column(db.DateTime,default=datetime.utcnow)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
#显示服务器名称信息
        return '<Server(name=%s)>'% self.name

    def save(self):
#保存到数据库
        db.session.add(self)
        db.session.commit()

    def delete(self):
#从数据库中删除
        db.session.delete(self)
        db.session.commit()
        
    @property
    def redis(self):
        return StrictRedis(host=self.host,port=self.port,password=self.password)
    
    def ping(self):
        #检查服务器是否可以访问
        try:
            return self.redis.ping()
        except ReidsError:
            raise RestException(400,'redis server %s can not connected' % self.host)
        
    def get_metrics(self):
        #获取Redis服务器监控信息
        try:
            return self.redis.info()
        except RedisError:
            raise RestException(400,'redis server %s can not connected' % self.host) 
