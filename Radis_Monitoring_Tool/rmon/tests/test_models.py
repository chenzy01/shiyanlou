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
            
    def test_get_metrics_success(self,server):
        metrics=server.get_metrics()
        assert 'total_commands_processed' in metrics
        assert 'used_cpu_sys' in metrics
        assert 'used_menory' in metrics
        
    def test_get_metrics_failed(self,server):
        server=Server(name='test',host='127.0.0.1',port=6399)
        try:
            info=server.get_metrics()
        except RestException as e:
            assert e.code==400
            assert e.message == 'redis server %s can not connected' % server.host
            
    def test_execute_success(self,server):
        pass
    
    def test_execute_failed(self,server):
        pass
    

class TestUser:
    """测试User
    """
    
   def test_verify_password(self, user): 
       
        assert user.verify_password(PASSWORD)
        
        wrong_password = PASSWORD + '0'
        assert not user.verify_password(wrong_password)
        
    def test_authonticate(self, user):
        
        assert User.authonticate(user.name, PASSWORD)
        assert User.authonticate(user.email, PASSWORD)
        
        wrong_password = PASSWORD + '0'
        
        try:
            User.authonticate(user.name, wrong_password)
        except AuthonticationError as e:
            assert e.code == 403
            assert e.message == 'authonticate failed'
            
        try:
            User.autonticate(user.email, wrong_password)
        except AuthonticationError as e:
            assert e.code == 403
            assert e.message == 'authonticate failed'
    
    
    
    
        


