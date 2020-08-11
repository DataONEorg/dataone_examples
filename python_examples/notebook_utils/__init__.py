# Base URLs of the Coordinating Node services for DataONE environments. 
# All but the "production" environment are for test purposes.
import textwrap

ENVIRONMENTS = {
    'dev'       : 'https://cn-dev.test.dataone.org/cn',
    'dev-2'     : 'https://cn-dev-2.test.dataone.org/cn',
    'sandbox'   : 'https://cn-sandbox.test.dataone.org/cn',
    'sandbox-2' : 'https://cn-sandbox-2.test.dataone.org/cn',
    'stage'     : 'https://cn-stage.test.dataone.org/cn',
    'stage-2'   : 'https://cn-stage-2.test.dataone.org/cn',
    'production': 'https://cn.dataone.org/cn',
}


def propertyStr(p):
    '''String representation of pyxb property
    '''
    if p is None:
        return ""
    try:
        return p.value()
    except:
        return str(p)

    
def nLines(t, max_lines=25):
    lines = t
    if isinstance(t, str):
        lines = t.split("\n")
    res = "\n".join(lines[:max_lines])
    if max_lines > 0:
        if len(lines) > max_lines:
            res += "\n...\n"
    return res


def asXml(o, max_lines=25):
    '''Return (partial) xml representation of pyxb object.
    
    Args:
      o (pyxb object): Object (e.g. response from DataONE service call)
      max_lines (int, optional): Maximum lines to return, all if 0 or less.
      
    Returns:
      Formatted XML (partial) representation of object
    '''
    return nLines(o.toDOM().toprettyxml(indent=' '*2), max_lines=max_lines)


def wrapText(t, indent=5, width=70):
    indent = " "*indent
    tw = textwrap.TextWrapper(
        width=width,
        initial_indent=indent,
        subsequent_indent=indent
    )
    return "\n".join(tw.wrap(t))

