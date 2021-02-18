import pprint
import json
from xml.dom.minidom import parseString

import yaml
import dicttoxml

from . import cfg

def python_print(name, data):
    pprint.pprint(data, indent=cfg.indent)

def json_print(name, data):
    print(json.dumps(data, indent=cfg.indent))
  
def yaml_print(name, data):
    print(yaml.safe_dump(data, indent=cfg.indent))

def xml_list_item(list_name):
    if list_name == 'colorgamut':
        return 'xy'
    elif list_name == 'xy':
        return 'coord'
    elif list_name[-1] == 's':
        return list_name[:-1]
    else:
        return 'item'
    
def xml_print(name, data):
    xml = dicttoxml.dicttoxml(data, custom_root=name,
                              attr_type=False, item_func=xml_list_item)
    dom = parseString(xml)
    print(dom.toprettyxml(indent=' '*cfg.indent))

formats = {
    'x':xml_print,
    'XML':xml_print,
    'p':python_print,
    'Python':python_print,
    'j':json_print,
    'JSON':json_print,
    'y':yaml_print,
    'YAML':yaml_print,
}
