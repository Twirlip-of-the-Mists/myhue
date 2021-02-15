class XMLPrint:
    """Class whose instances print a restricted set of python data stuctures
    in something similar to, but not identical to, XML.
    
    It only handles dicts, lists and a few basic types.
    
    Dicts have to have keys that are valid XML tag names.
    
    List items have a default tag of "listitem", but that can be changed
    by adding tag names to the listitems dict.
    
    For example this:
    
        xml_print = XMLPrint()
        xml_print.listitems['colours'] = 'colour'
        xml_print.pprint('car', {'model':'Mini', 'colours':['red', 'green']})
      
    Outputs this:
    
        <car>
            <model>Mini</model>
            <colours>
                <colour>red</colour>
                <colour>green</colour>
            </colours>
        </car>
    """
    def __init__(self, indent_str='    '):
        """Create an XML printer, with a pprint method that prints stuff.
        """        
        self.indent_str = indent_str
        self.listitem = 'listitem'
        self.listitems = dict()
        self.stringize = [bool, str, int, float]
    
    def sanitize(self, name):
        # FIXME: What about '/' & '>' characters, and other stuff?
        return name.replace(' ', '_')
  
    def open_tag(self, name, data, types):
        if types:
            return f'<{self.sanitize(name)} type="{data.__class__.__name__}">'
        else:
            return f'<{self.sanitize(name)}>'

    def close_tag(self, name):
        return f'</{self.sanitize(name)}>'

    def empty_tag(self, name):
        return f'<{self.sanitize(name)}/>'
  
    def indentation(self, indent):
        return self.indent_str * indent
  
    def pprint(self, name, data, indent=0, types=False):
        """Print a data object in XML.
        
        The top level tag will be "name".
        
        To include tag attibutes specifying the data type, pass types=True
        """
        classname = data.__class__.__name__
        printer = getattr(self, f'pp_{data.__class__.__name__}', self.pp_unknown)
        printer(name, data, indent, types)
    
    def pp_unknown(self, name, data, indent, types):
        if data is None:
            print(f'{self.indentation(indent)}{self.empty_tag(name)}')
        elif type(data) in self.stringize :
            print(f'{self.indentation(indent)}{self.open_tag(name, data, types)}{data}{self.close_tag(name)}')
        else:
            raise ValueError(f'Unhandled type "{data.__class__.__name__}"')

    def pp_dict(self, name, data, indent, types):
        print(f'{self.indentation(indent)}{self.open_tag(name, data, types)}')
        for key, value in data.items():
            self.pprint(key, value, indent+1)
        print(f'{self.indentation(indent)}{self.close_tag(name)}')
    
    def pp_list(self, name, data, indent, types):
        print(f'{self.indentation(indent)}{self.open_tag(name, data, types)}')
        for item in data:
            self.pprint(self.listitems.get(name, self.listitem), item, indent+1)
        print(f'{self.indentation(indent)}{self.close_tag(name)}')

if __name__ == '__main__':
    xml_print = XMLPrint()

    xml_print.pprint('car', {'model':'Golf', 'colours':['blue', 'white']})

    print()

    xml_print.listitems['colours'] = 'colour'
    xml_print.pprint('car', {'model':'Mini', 'colours':['red', 'green']})
