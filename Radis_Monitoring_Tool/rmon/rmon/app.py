#创建并初始化 Flask 应用的代码

import os
from flask import Flask
from rmon.views import api
from rmon.models import db
from rmon.config import DevConfig,ProductConfig

def create_app():
#创建并初始化了Flask App
    app=Flask('rmon')
#根据环境变量加载开发环境变量或者生产环境变量
    env=os.environ.get('RMON_ENV')

    if env in ('pro','prod','product'):
        app.config.from_object(ProductConfig)
    else:
        app.config.from_object(DevConfig)
#
    app.config.from_envvar('RMON_SETTINGS',silent=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#注册蓝图
    app.register_blueprint(api)
#初始化数据库    
    db.init_app(app)
#如果是开发环境就创建所有数据库表
    if app.debug:
        with app.app_context():
            db.create_all()
    return app
