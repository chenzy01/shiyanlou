
import json
ifrom flask import url_for 
 
from rmon.models import Server


class TestIndex:
    #测试首页，渲染模板
    endpoint=='api.index'

    def test_index(self,client):
        resp=client.get(url_for(self.endpoint)
        assert resp.status_code==200
        #模板渲染成功并返回
        assert b'<div id="app"></div>' in resp.data
  
class TestServerList:
#测试Redis服务列表API
    endpoint='api.server_list'

    def test_get_servers(self,server,client):
        #获取Redis服务器列表
        resp=client.get(url_for(self.endpoint))

        assert resp.headers['Content-Type']=='application/json;charset=utf-8'
        #访问成功后返回状态码：200 OK
        assert resp.status_code==200
        servers=resp.json
        assert len(servers)==1
        h=servers[0]
        assert h['name']==server.name
        assert h['description']==server.description
        assert h['host']==server.host
        assert h['port']==server.port
        assert 'updated_at' in h
        assert 'created_at' in h

    def test_create_server_success(self,db,client):
        #测试创建Redis服务器成功
        #查询数据库，无记录 
        assert Server.query.count()==0
        #用于创建Redis服务器的参数
        data={
            'name':'Redis测试服务器'
            'description':'这是一台服务器'
            'host':'127.0.0.1'
        }
        #通过 '/server/'接口创建Redis服务器
        resp=client.post(url_for(self.endpoint),
                         data=json.dump(data),
                         content_type='application/json')
        #创建Redis服务器成功，返回状态码201
        assert resp.status_code==201
        assert resp.json=={'ok':True}
        #成功写入数据库
        assert Server.query.count()==1
        server=Server.query.first()
        assert server is not None
        for key in data:
            assert getattr(server,key)==data[key]

    def test_create_server_failed_with_invalid_host(self,db,client):
    #无效的服务器地址导致创建Redis服务器失败
    #地址无效时，返回错误信息
        errors={'host':'String does not match expected pattern.'}
                        
        #用于创建Redis服务器的参数
        data={
            'name':'Redis测试服务器'
            'description':'这是一台服务器'
            #无效的IP地址
            'host':'127.0.0.1234'
        }
                        
    #通过 '/server/'接口创建Redis服务器
        resp=client.post(url_for(self.endpoint),
                         data=json.dump(data),
                         content_type='application/json')
        assert resp.status_code==400
        assert resp.json==errors

    def test_cerate_server_failed_with_duplciate_server(self,server,client):
    #创建重建的服务器时将失败
        #创建失败时返回的错误
        errors={'host':'Redis server already exist.'}
                        
        #用于创建Redis服务器的参数
        data={
            'name':server.name
            'description':'重复的Redis服务器'
            'host':'127.0.0.1'
        }
        #通过 '/server/'接口创建Redis服务器
        resp=client.post(url_for(self.endpoint),
                         data=json.dump(data),
                         content_type='application/json')
        assert resp.status_code==400
        assert resp.json==errors


class TestServerDetail:
    #测试Redis服务器详情API
    endpoint='api.server_detail'

    def test_get_server_success(self,server,client):
        #测试获取Redis服务器详情
        url=url_for(self.endpoint,object_id=server.id)
        resp=client.get(url)
        assert resp.status_code==200
        
        data=resp.json
        for key in ('name','description','host','port'):
            assert data[key]==getattr(server,key)
                        
    def test_get_server_failed(self,db,client):
        #获取不存在的Redis服务器详情失败
        errors={'ok':False,'message':'object not exist'}
        server_not_exist=100
        url=url_for(self.endpoint,object_id=server_not_exist)
        resp=client.get(url)
        #Redis服务器不存在时返回404          
        assert resp.status_code==404
        assert resp.json==errors
        
    def test_update_server_success(self,server,client):
        #更新Redis服务器成功
        data={'name':'更新后的服务器'}
        assert server.name != data['name']
        assert Server.query.count()==1
        #通过 '/server/'接口创建Redis服务器
        resp=client.put(url_for(self.endpoint,object_id=server.id),
                         data=json.dumps(data),
                         content_type='application/json')
        assert resp.status_code==200
        #成功更新名称
        assert server.name==data['name']
                        
    def test_update_server_success_with_duplicate_server(self,server,client):
        #更新服务器名称为其它同名服务器名称时失败
        errors={'name':'Redis server already exist'}
        assert Server.query.count()==1
        #先创建Redis服务器
        second_server=Server(name='second_server',description='test',
                             host='192.168.0.1',port=6379)
        second_server.save()
        assert Server.query.count()==2
        #尝试将second_server的名称更新成server,将会失败               
        data={'name':server.name}
        #通过 '/server/'接口创建Redis服务器
        resp=client.put(url_for(self.endpoint,object_id=second_server.id),
                         data=json.dumps(data),
                         content_type='application/json')
        assert resp.status_code==400
        assert resp.json==errors
                        
    def test_delete_success(self,server,client):
        #删除Redis服务器成功
        assert Server.query.count()==1
        resp=client.delete(url_for(self.endpoint,object_id=server.id)
        assert resp.status_code==204
        assert Server.query.count()==0                   
                        
    def test_delete_failed_with_host_not_exist(self,db,client):
        #删除不存在的Redis服务器失败
        errors={'ok':False,'message':'object not exist'}
        server_not_exist=100
        assert Server.query.get(server_not_exist) is None
        
        resp=client.delete(url_for(self.endpoint,object_id=server_not_exist))
        
        assert resp.status_code==404                   
        assert resp.json==errors                   
                           
class TestServerMetrics:                           
    #测试Redis监控信息API
    
    endpoint='api.server_metrics'                          
    
    def test_get_metrics_success(self,server,client):
        #成功获取Redis服务器监控信息                   
        resp=client.get(url_for(self.endpoint,object_id=server.id))
        assert resp.status_code==200                  
        metrics=resp.json           
        #refer https://redis.io/commands/INFO                   
        assert 'total_commands_processed' in metrics                   
        assert 'used_cpu_sys' in metrics                  
        assert 'used_memory' in metrics                   
        
    def test_get_metrics_failed_with_server_not_exist(self,db,client):                     
        #获取不存在的Redis服务器监控信息失败                   
        errors={'ok':False,'message':'object not exist'}                   
        server_not_exist=100                   
        assert Server.query.get(server_not_exist) is None                   
        resp =client.get(url_for(self.endpoint,object_id=server_not_exist))                   
        assert resp.status_code==404                   
        assert resp.json==errors
                           
                           
class TestServerCommand:
    #测试Redis服务器执行命令接口  
                           
    endpoint='api.server_command'                          
                           
                           
