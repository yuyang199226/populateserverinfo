import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_ITEMS={
    'disk':'src.plugins.disk.Disk',
    'memory':'src.plugins.memeory.Memory',
    'nic':'src.plugins.nic.Nic',
    'basic':'src.plugins.basic.Basic',
    'board':'src.plugins.board.Board',
}
API='http://127.0.0.1:8000/api/assetinfo/'
MODE = 'ssh'   #SSH or agent or saltstack
DEBUG=True
SSH_HOST = '192.168.16.172'
SSH_PORT=22
SSH_USERNAME='root'
SSH_PWD='1055979970yy'

