#!/usr/bin/python
#-*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
#��ʼ�����ݿ�����
engine=create_engine('mysql+mysqldb://root@localhost:3306/shiyanlou?charset=utf8')
#��������Ļ���
Base= declarative_base()
#����items.py ����Course Model����
class Course(Base):
    __tablename__='courses'
#��Ľṹ
    id=Column(Integer,primary_key=True)
    name=Column(String(64),index=True)
    description=Column(String(1024))
    type=Column(String(64),index=True)
    students=Column(Integer)


if __name__=='__main__':
#���û��ഴ����    
    Base.metadata.create_all(engine)
