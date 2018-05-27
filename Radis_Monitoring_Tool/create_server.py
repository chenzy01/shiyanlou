import requests


CREATER_SERVER='http://127.0.0.1:5000/servers/'

def creater_server(name,host):
    data={
        'name':name
        'host':host
            }

    resp=requests.port(CREATER_SERVER,json=data)
    return resp.json()


