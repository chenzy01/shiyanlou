"""

本项目将实现一个 Redis 服务器监控应用 rmon，该应用可以管理多台 Redis 服务器，并监控 Redis 服务器的状态。

项目开始前，安装虚拟环境和依赖软件包
$ virtualenv -p /usr/bin/python3 venv
$ pip install -r requirements.txt

项目机构信息：

项目目录为 /.../rmon;

项目中包含核心代码 rmon 模块;

rmon.models 模块包含了所有的数据库定义;

rmon.views 模块包含了所有的视图控制器代码;

rmon.config 模块包含了所有的配置信息代码;

rmon.app 模块实现了创建 Flask 应用的函数 create_app;

rmon/templates 目录包含所有的模板文件;

rmon/frontend 目录包含所有的前端界面实现代码，目前是一个空目录;

rmin/static 目录包含所有的静态文件，比如 javascript 文件

"""
