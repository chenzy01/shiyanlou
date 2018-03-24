#ʹ��sqlalchemy�������ݿ���ͨ��Engine�������
from sqlalchemy import create_engine
engine=create_engine('mysql://root:@localhost/shiyanlou')
engine.execute('select * from user').fetchall()

#����declarative base class����python�࣬���Զ�ӳ�䵽��Ӧ�����ݿ���
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()

from sqlalchemy import Column,Integer,String
#����User�ಢӳ�䵽user��
class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
    def __repr__(self):
        return "<User(name=%s)>" % self.name
