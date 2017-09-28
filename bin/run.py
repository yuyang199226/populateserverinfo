import os
import sys
import requests

os.environ['AUTO_CLIENT_SETTINGS']= 'conf.settings'

from lib.config import settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from src.plugins import handle_plugin
from src import script

if __name__ == '__main__':
   script.start()





# import subprocess
# import requests
# ret = subprocess.getoutput('ipconfig')
# ret=ret[40:50]
# requests.post(url='http://127.0.0.1:8000/api/assetinfo/',data={'k1':ret})