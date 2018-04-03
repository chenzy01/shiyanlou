#!/usr/bin/python
#-*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy import Date

#初始化数据库链接
engine=create_engine('mysql+mysqldb://root@localhost:3306/shiyanlou?charset=utf8')
#创建对象的基类
Base= declarative_base()
#根据items.py 创建Course Model对象
class Course(Base):
    __tablename__='courses'
#表的结构
    id=Column(Integer,primary_key=True)
    name=Column(String(64),index=True)
    description=Column(String(1024))
    type=Column(String(64),index=True)
    students=Column(Integer)

#创建User表
class User(Base):
    __tablename__='users'
    
    id=Column(Integer,primary_key=True)
    name=Column(String(64),index=True)
    type=Column(String(64))
    status=Column(String(64),index=True)
    school=Column(String(64))
    job=Column(String(64))
    level=Column(Integer,index=True)
    join_date=Column(Date)
    learn_courses_num=Column(Integer)

if __name__=='__main__':
#利用基类创建表    
    Base.metadata.create_all(engine)
