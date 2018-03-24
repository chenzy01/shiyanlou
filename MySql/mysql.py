#使用sqlalchemy连接数据库是通过Engine对象进行
from sqlalchemy import create_engine
engine=create_engine('mysql://root:@localhost/shiyanlou')
engine.execute('select * from user').fetchall()

#基于declarative base class创建python类，会自动映射到相应的数据库上
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()

from sqlalchemy import Column,Integer,String
#创建User类并映射到user表
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    def __repr__(self):
        return "<User(name=%s)>" % self.name
