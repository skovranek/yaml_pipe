from typing import Any


def key_search(node: Any, key: Any):
    t = type(node)
    if t == type({}):
        if key in node:
            return node[key], [str(key)], True
        for k in node:
            value, path, found = key_search(node[k], key)
            if found:
                return value, [str(k)] + path, True
    if t == type([]):
        for i, element in enumerate(node):
            value, path, found = key_search(element, key)
            if found:
                return value, [i] + path, True
    return None, [], False
