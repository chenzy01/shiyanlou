""" rmon.views.auth

实现用户认证登录功能
"""

from datetime import datetime
from flask import request

from rmon.models import User
from rmon.common.errors import AuthenticationError
from rmon.common.rest import RestView


class AuthView(RestView):
    """认证视图控制器
    """

    def post(self):
        """登录认证用户

        用户可以使用昵称或者邮箱进行登录，登录成功后返回用于后续认证的 token
        """
        #检查data数据
        data = request.get_json()
        if data is None:
            raise AuthenticationError(403, 'user or password required')
            
        name = data.get('name')
        password = data.get('password')

        if not name or not password:
            raise AuthenticationError(403, 'user name or password required')

        #只有管理员用户允许登录管理后台
        user = User.authenticate(name, password)
        if not user.is_admin:
            raise AuthenticationError(403, 'user name or password required')
            
        user.login_at = datetime.utcnow()
        user.save()
        return {'ok': True, 'token': user.generate_token()}
