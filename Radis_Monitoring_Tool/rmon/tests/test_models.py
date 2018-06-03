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
            
    def test_generate_token(self, user, app):
        """测试 User.generate_token 方法
        """
        now = timegm(datetime.utcnow().utctimetuple())
        token = user.generate_token()
        
        payload = jwt.decode(token, verify=False)
    
        assert payload['uid'] == user.id
        assert payload['is_admin'] == user.is_admin
        assert 'refresh_exp' in payload
        assert 'exp' in payload
        
        # 生成的 token 有效期为一天
        assert payload['exp'] - now == 24*3600
        # token 过期后十分钟内，还可以使用老 token 进行刷新 token
        assert payload['refresh'] - now == 24 * 3600 + 10 * 60
        u = User.verify_token(token)
        assert u == user
        
    def test_verify_token(self,user):
        """测试 User.verify_token 类方法
        """
        
        # 成功验证 token
        token = user.generate_token()
        # 验证 token 成功后会返回 User 对象
        u = User.verify_token(token)
        assert user == u
        
    def test_verify_token_failed(self,user,app):
        """测试 User.verify_token 验证 token 时失败
        """
        
        algorithm = 'HS512'
        
        #token 验证失败
        invalid_token = user.generate_token() + '0'
        
        try:
            User.verify_token(invalid_token)
        except InvalidTokenError as e:
            assert e.code == 403
            assert 'Signature' in e.message
            
        #token 指定用户不存在
        exp = datetime.utcnow() + timedelta(days=1)
        # token 过期后十分钟内，还可以使用老 token 进行刷新 token
        refresh_exp = timegm(exp + timedelta(seconds=60*10)).utctimetuple())
        
        #用户不存在
        user_not_exist = 100
        payload = {
            'uid' : user_not_exist,
            'is_admin' : False,
            'exp' : exp,
            'refresh' : refresh_exp
            }
        
        #用户不存在
        try:
            User.verify_token(jwt.encode(payload, app.secret_key, algorithm = algorithm))
        except InvalidTokenError as e:
            assert e.code == 403
            assert e.message == 'user not exist'
            
        payload = {'exp' : exp}
        try:
            User.verify_token(jwt.encode(payload, app.secret_key,algorithm = aogorithm))
        excpet InvalidTokenError as e:
            assert e.code == 403
            assert e.message == 'invalid token'
            
        # token 刷新时间无效
        refresh_exp = datetime.utcnow() - timedelta(days=1)
        
      
    
