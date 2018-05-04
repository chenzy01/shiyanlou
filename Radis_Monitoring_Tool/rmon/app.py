"""
app.py,应用程序入口文件
"""

import urllib
from rmon.app import create_app
from rmon.models import db

app=create_app()

@app.cli.command()
def routes():
    #app中定义的所有路由
    output=[]
    for rule in app.url_map.iter_rules():
        methods=','.join(rule.methods)
        line=urllib.parse.unquote("{:25s} {:35s} {:20s}".format(rule.endpoint,methods,str(rule)))
        output.append(line)
        
    for line in sorted(output):
        print(line)
    
def init_db():
#初始化数据库
    print("sqlite3 database file is %s" % app.fonfig['SQLALCHEMY_DATABASE_URI'])
    db.create_all()
