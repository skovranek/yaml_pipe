#from argcomplete import warn
from argparse import Namespace
from typing import Any, List, Set

from .load_yaml import load
from .access_keys import access_keys


def populate_keys(prefix: str, parsed_args: Namespace, **kwargs: str) -> Set[str]:
#def populate_keys(prefix, parsed_args, **kwargs):
    """Load yaml and return keys for autocompletion."""
    #warn('populate called')
    if parsed_args.file:
        data = load(parsed_args.file)
        if parsed_args.keys and len(parsed_args.keys) > 0:
            nested_node, exists = access_keys(data, parsed_args.keys)
            if exists:
                data = nested_node
        return (x for x in keys_or_indices(data) if x.startswith(prefix))
    return ()


def keys_or_indices(node: Any) -> List[str]:
    t = type(node)
    # sequence
    if t == type([]):
        return [str(i) for i in range(len(node))]
    # mapping
    if t == type({}):
        return [str(k) for k in node.keys()]
    # scalar
    return []
