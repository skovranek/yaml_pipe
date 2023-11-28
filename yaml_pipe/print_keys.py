from typing import Any


def print_keys(node: Any):
    """Print keys, elements, or scalar value."""
    t = type(node)
    # sequence
    if t == type([]):
        for i, element in enumerate(node):
            print(f'{i} - {str(element)}')
        return
    # mapping
    if t == type({}):
        for key in node:
            print(str(key))
        return
    # scalar
    print(str(node))
    return
