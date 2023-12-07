import json
import re
from string import Template


def find(data):
    if isinstance(data, dict):
        data = json.dumps(data)
        pattern = "\\${(.*?)}"
        return re.findall(pattern, data)


def replace(ori_data, replace_data):
    ori_data = json.dumps(ori_data)
    s = Template(ori_data)
    return s.safe_substitute(replace_data)


def parse_relation(var, restdata):
    if not var:
        return restdata
    else:
        restdata = restdata.get(var[0])
        del var[0]
        return parse_relation(var, restdata)

if __name__ == '__main__':
    s = Template('${who} 在 ${do}')
    ts = s.substitute(who="张三", do="赏花")
    print(ts)