#定义所有API对应的URL

from flask import Blueprint
from rmon.views.index import IndexView

api=Blueprint('api',__name__)
#定义路由规则
api.add_url_rule('/',view_func=IndexView.as_view('index'))
