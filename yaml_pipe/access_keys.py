from sys import stderr
from typing import Any, List


e = 'key error: '
ie = 'index error: '

def access_keys(node: Any, keys: List[str]) -> Any:
        """Keys list contains strings that are dict keys or list indices."""
        if len(keys) != 0:
            key = keys.pop(0)
            lastkey = len(keys) == 0
            t = type(node)
            try:
                if t == type({}):
                    if key in node:
                        value = node[key]
                        if lastkey:
                            return value, True
                        else:
                            return access_keys(value, keys)
                    if key[0] in '0123456789-.':
                        if key.count('.') < 2:
                            if all(x in '0123456789.' for x in key[1:]):
                                integer = float(key)
                            if integer in node:
                                value = node.get(integer)
                                if lastkey:
                                    return value, True
                                else:
                                    return access_keys(value, keys)
                    elif key == 'True' or key == 'true':
                        if True in node:
                            value = node.get(True)
                            if lastkey:
                                return value, True
                            else:
                                return access_keys(value, keys)
                    elif key == 'False' or key == 'false':
                        if False in node:
                            value = node.get(False)
                            if lastkey:
                                return value, True
                            else:
                                return access_keys(value, keys)
                    elif key == 'None' or key == 'null':
                        if None in node:
                            value = node.get(None)
                            if lastkey:
                                return value, True
                            else:
                                return access_keys(value, keys)
                    else:
                        stderr.write(
                            f"{e}key '{key}' not found in mapping/dict.\n"
                        )

                if t == type([]):
                    if key[0] in '0123456789-':
                        if all(x in '0123456789' for x in key[1:]):
                            index = int(key)
                            ln = len(node)
                            if (index >= 0 and ln > index) \
                                or (index < 0 and abs(index) <= ln):
                                element = node[index]
                                if lastkey:
                                    return element, True
                                else:
                                    return access_keys(element, keys)
                            else:
                                stderr.write(
                                    f"{ie}index '{key}' out of range [0, {ln}].\n"
                                )
                    else:
                        stderr.write(
                            f"{ie}could not parse index '{key}'.\n"
                        )
                else:
                    stderr.write(f"{e}node is not a collection.\n")
            except:
                stderr.write(
                    f'{e}key or index not found because key arg could not be parsed.\n'
                )
                return node, False
        else:
            stderr.write(f'{e}no key or index passed as argument.\n')
        return node, False
