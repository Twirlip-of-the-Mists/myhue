import pprint
import json
from xml.dom.minidom import parseString

import yaml
import dicttoxml

INDENT = 2 # FIXME This should be an option

def python_print(name, data, indent=INDENT):
    pprint.pprint(data, indent=indent)

def json_print(name, data, indent=INDENT):
    print(json.dumps(data, indent=indent))
  
def yaml_print(name, data, indent=INDENT):
    print(yaml.safe_dump(data, indent=indent))

def xml_list_item(list_name):
    if list_name == 'colorgamut':
        return 'xy'
    elif list_name == 'xy':
        return 'coord'
    elif list_name[-1] == 's':
        return list_name[:-1]
    else:
        return 'item'
    
def xml_print(name, data, indent=INDENT):
    xml = dicttoxml.dicttoxml(data, custom_root=name,
                              attr_type=False, item_func=xml_list_item)
    dom = parseString(xml)
    print(dom.toprettyxml(indent=' '*indent))

formats = {
    'XML':xml_print,
    'Python':python_print,
    'JSON':json_print,
    'YAML':yaml_print,
}
