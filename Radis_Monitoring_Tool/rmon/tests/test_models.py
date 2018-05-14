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
        
    def test_ping_success(self,db,sever):
#Server.ping方法执行成功，需保证Redis服务器监听在 127.0.0.1:6379地址
        assert server.ping() is True
    
    def test_ping_failed(sefl,db):
#Server.ping 方法执行失败，会抛出 RedisException异常
        server=Server(name='test',host='127.0.0.1',port=6399)
        try:
            server.ping()
        excep RestException as e:
            assert e.code == 400
            assert e.message == 'redis server %s cannot connected' % server.host

