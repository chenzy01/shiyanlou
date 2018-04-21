#!usr/bin/python3
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy import DateTime

engine=create_engine('mysql+mysqldb://root@localhost:3306/shiyanlougithub?charset=utf8')

Base=declarative_base()

class Repository(Base):
    __table__='repositories'
    id=Column(Integer,primary_key=True)
    name=Column(String(64))
    update_time=Column(DateTime)
    commits=Column(Integer)
    branches=Column(Integer)
    releases=Column(Integer)

if __name__=='main':
    Base.metadata.create_all(engine)


