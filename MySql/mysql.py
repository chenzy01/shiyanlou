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

#引入Session查询数据库
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(bind=engine)
session=Session()

#多表关联、查询
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
#课程表
class Course(Base):
    __tablename__='course'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    teacher_id=Column(Integer,ForeignKey('user_id'))
    teacher=relationship('User')
    def __repr__(self):
        return "<Course(name=%s)>" % self.name
#实验表    
class Lab(Base):
    __tablename__='lab'
    id=Column(Integer,primary_key=True)
    name=Column(String(64))
    course_id=Column(Integer,ForeignKey('course_id'))
#backref参数，该参数使得可以在 Course 实例中，通过 course.labs 访问关联的所有实验记录。
    course=relationship('Course',backref='labs')
    def __repr__(self):
        return "<Lab(name=%s)>" % self.name

#用户附属信息表
class UserInfo(Base):
    __tablename='userinfo'
    user_id=Column(Integer,ForeignKey('user_id'),primary_key=True)
    addr=Column(String(512))
    
#课程表和标签关联 
 from sqlalchemy import Table,Text
 course_tag=Table('course_tag',Base.metadata,
                  Column('course_id',ForeignKey('course.id'),primary_key=True),
                  Column('tag_id',ForeignKey('tag.id'),primary_key=True)
                 )

#标签表
class Tag(Base):
    __tablename__='tag'
    id=Column(Integer,primary_key=True)
    name=Column(String(64))
    courses=relationship('Course',secondary=course_tag,backref='tags')
    def __repf__(self):
        return "<Tag(name=%s)>" % self.name
    
#创建表
Base.metadata.create_all(engine)
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
                         
