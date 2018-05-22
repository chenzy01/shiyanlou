
import json
ifrom flask import url_for 
 
from rmon.models import Server


class TestServerList:

    endpoint='api.server_list'

    def test_get_servers(self,server,client):
        resp=client.get(url_for(self.endpoint))

        assert resp.headers['Content-Type']=='application/json;charset=utf-8'
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
        pass

    def test_create_server_failed_with_invalid_host(self,db,client):
        pass

    def test_cerate_server_failed_with_duplciate_server(self,server,client):
        pass


class TestServerDetail:
    endpoint='api.server_detail'

    def test_get_server_success(self,server,client):
        pass

    def test_get_server_failed(self,db,client):
        pass

    def test_update_server_success(self,server,client):
        pass

    def test_update_server_success_with_duplicate_server(self,server,client):
        pass

    def test_delete_failed_with_host_not_exist(self,db,client):
        pass

