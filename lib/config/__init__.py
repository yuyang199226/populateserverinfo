import os
import importlib
from . import global_settings

class Setting(object):
    '''将配置文件中的所有属性拿到，设置为Setting的属性'''
    def __init__(self):
        for item in dir(global_settings):
            if item.isupper():
                k=getattr(global_settings,item)
                setattr(self,item,k)
        setting_path = os.environ.get('AUTO_CLIENT_SETTINGS')
        setting_module = importlib.import_module(setting_path)
        for item in dir(setting_module):
            if item.isupper():
                v = getattr(setting_module,item)
                setattr(self,item,v)


settings=Setting()