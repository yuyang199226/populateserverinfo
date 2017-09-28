import requests
from concurrent.futures import ThreadPoolExecutor
from lib.config import settings
from src.plugins import handle_plugin


class BaseClient(object):
    def __init__(self):
        self.API = settings.API
    def excute(self):
        raise NotImplemented('必须实现excute方法')
    def post_server_info(self,data):
        requests.post(url=self.API,json=data)

class AgentClient(BaseClient):
    def excute(self):
        ret = handle_plugin()
        return ret

class SshSaltstackClient(BaseClient):
    def task(self,host):
        data = handle_plugin(host)
        self.post_server_info(data)

    def get_host_list(self):
        '''从api获取要检测信息的主机名
        待完成'''
        host=['abc.com']
        return host

    def excute(self):
        pool= ThreadPoolExecutor(8)
        host_list = self.get_host_list()
        for host in host_list:
            pool.submit(self.task,host)


