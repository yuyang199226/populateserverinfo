import importlib
import paramiko
import subprocess
import traceback
from lib.config import settings


def excute_cmd(cmd,host=None):
    if settings.MODE == 'ssh':
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=settings.SSH_PORT, username=settings.SSH_USERNAME,
                    password=settings.SSH_PWD)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        ssh.close()

    elif settings.MODE == 'agent':
        result = subprocess.getoutput(cmd)

    elif settings.MODE == 'saltstack':
        result = subprocess.getoutput('salt "c1.com" cmd.run %s' %cmd)

    else:
        raise Exception('conf.settings.EXCUTE_MODE is not correct')
    return result
def handle_plugin(host=None):
    dic_info={}
    for k,v in settings.PLUGIN_ITEMS.items():
        data = {
            'status': True,
            'msg': None,
            'error_msg': None,
        }
        try:
            module_path,class_name = v.rsplit('.',maxsplit=1)
            ret = importlib.import_module(module_path)
            cls_obj = getattr(ret,class_name)
            data['msg'] = cls_obj().process(excute_cmd,settings.DEBUG,host)
        except Exception as e:
            data['status']=False
            data['error_msg'] = traceback.format_exc()

        dic_info[k] = data
    return dic_info