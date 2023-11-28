from typing import Any


def print_nodes(node: Any, i: int = 0, islist: bool = False):
    """Iterate through yaml to print."""
    indent = i * ' '
    # - bullet point elements of sequence
    if islist:
        indent = ((i-2) * ' ') + '- '
    t = type(node)
    # sequence
    if t == type([]):
        for element in node:
            print_nodes(element, i + 2, True)
        return
    # mapping
    if t == type({}):
        for key in node:
            k = str(key)
            val = node[key]
            valtype = type(val)
            # mapping
            if valtype == type({}):
                print(indent + k + ':')
                print_nodes(val, i + 2, False)
            # sequence
            elif valtype == type([]):
                print(indent + k + ':')
                print_nodes(val, i + 2, True)
            # multiline string
            elif valtype == type('') and '\n' in val:
                print(indent + k + ':')
                multiline = val.split('\n')
                for line in multiline:
                    print(((i+2) * ' ') + line)
            # any other scalar
            else:
                print(indent + k + ': ' + str(val))
            indent = i * ' '
        return
    # multiline string
    if t == type('') and '\n' in node:
        multiline = node.split('\n')
        for line in multiline:
            print(indent + line)
            indent = i * ' '
        return
    # any other scalar
    print(indent + str(node))
    return
