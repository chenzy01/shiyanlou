#测试用例
from rmon.models import Server
from rmon.common.rest import RestException


class TestServer:
#测试Server相关功能

    def test_save(self,db):
#测试Server.save 保存服务器方法
        assert Server.query.count()==0
        server=Server(name='test',host='127.0.0.1')
        server.save()
        assert Server.query.count()==1
        assert Server.query.first()==server

    def test_delete(self,db,server):
#测试Server.delete 删除服务器方法
        assert Server.query.count()==1
        server.delete()
        assert Server.query.count()==0
        
    


