from lib.config import settings
import os


class Board(object):
    def process(self,excute_cmd,debug,host=None):
        if debug:
            output = open(os.path.join(settings.BASE_DIR, 'files/board.out'), 'r', encoding='utf-8').read()
        else:
            output = excute_cmd("sudo dmidecode -t1",host)

        return self.parse(output)

    def parse(self, content):

        result = {}
        key_map = {
            'Manufacturer': 'manufacturer',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }

        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]

        return result
