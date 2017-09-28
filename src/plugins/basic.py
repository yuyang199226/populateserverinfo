
class Basic(object):

    @classmethod
    def initial(cls):
        return cls()

    def process(self,cmd_func,test,host):
        if test:
            output = {
                'os_platform': "linux",
                'os_version': "CentOS release 6.6 (Final)\nKernel \r on an \m",
                'hostname': 'c1.com'
            }
        else:
            output = {
                'os_platform': cmd_func("uname",host).strip(),
                'os_version': cmd_func("cat /etc/issue",host).strip().split('\n')[0],
                'hostname': cmd_func("hostname",host).strip(),
            }
        return output

