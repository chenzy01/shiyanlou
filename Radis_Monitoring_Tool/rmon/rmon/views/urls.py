#定义所有API对应的URL

from flask import Blueprint

from rmon.views.index import IndexView
from rmon.views.server import （ServerList，ServerDetail，ServerCommand,ServerMetrics）
from rmon.views.wx import WxView


api=Blueprint('api',__name__)
#定义路由规则
api.add_url_rule('/',view_func=IndexView.as_view('index'))

api.add_url_rule('/server/',view_func=ServerList.as_view('server_list'))

api.add_url_rule('/server/<int:object_id>',
                 view_func=ServerDetail.as_view('server_detail'))

api.add_url_rule('/server/<int:object_id>/metrics',
                 view_fucn=ServerMetrics.as_view('server_metrics'))

api.add_url_rule('/server/<int:object_id>/command',
                 view_fucn=ServerCommand.as_view('server_command'))

# 登录
api.add_url_rule('/login', view_func=AuthView.as_view('login'))

#微信消息回调地址
api.add_url_rule('/wx/',view_func=WxView.as_view('wx_view'))

