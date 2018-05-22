#定义所有API对应的URL

from flask import Blueprint
from rmon.views.index import IndexView
from rmon.views.server import ServerList
from rmon.views.server import ServerDetail


api=Blueprint('api',__name__)
#定义路由规则
api.add_url_rule('/',view_func=IndexView.as_view('index'))

api.add_url_rule('/server/',view_func=ServerList.as_view('server_list'))

api.add_url_rule('/server/<int:object_id>',view_func=ServerDetail.as_view('server_detail'))


