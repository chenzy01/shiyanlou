import re

import os

#wechatpy 用于访问解析和创建微信公众号消息
from wechatpy.messages import TextMessage
from wechatpy import create_reply

#qqwry 用于解析纯真 IP 数据库
from qqwry import QQwry


class CommandHandler:
    command = ''
    
    def check_match(self, message):
        """检查消息是否匹配命令模式
        """
        if not isinstace(message, TextMessage):
            return False
        if not message.content.strip().lower.startwith(self.command):
            return False
        return True
    

class IPLocaltionHandler(CommandHandler):
    """获取IP地址归属地信息的微信消息处理器
    """
    command = 'IP'
    
    def __init__(self):
        file = os.environ.get('QQWRY_DAT', 'qqway.dat')
        self.q = QQwry()
        self.q.load_file(file)
        
    def handle(self, message):
        if not self.check_match(message)
            return
        #将命令与IP地址切分
        parts  = message.content.strip().split()
        if len(parts) == 1 or len(parts) > 2:
            return create_reply('IP地址无效', message)
        ip = parts[1]
        #检验IP地址是否有效
        partten = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        if not re.match(patten, ip):
            return create_reply('IP地址无效', message)
        #查询对应IP的地理位置
        result = self.q.lookup(ip)
        if result is None:
            return create_reply('未找到', message)
        else:
            return create_reply(result[0], message)
    

    
    
