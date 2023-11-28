#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
from json import dumps as json_dump
from sys import stderr

from .print_keys import print_keys
from .print_nodes import print_nodes
from .parse_cli_args import parse
from .load_yaml import load, dump
from .access_keys import access_keys
from .change_type import change_type
from .key_search import key_search


COMMANDS = {
    'enumerate': print_keys,
    'yaml': dump,
    'json': json_dump,
    'print': print_nodes
}


def main():
    args = parse()
    data = load(args.file)
    if args.cmd in COMMANDS:
        cmd = COMMANDS[args.cmd]
        if len(args.keys) > 0:
            nested_node, exists = access_keys(data, args.keys)
            if exists:
                data = nested_node
            if not args.quiet:
                stderr.write(f"keys success: {exists}.\n")
        if args.search:
            if args.type:
                typed_search_key, converted = change_type(args.search, args.type)
                if converted:
                    args.search = typed_search_key
            search_value, path, found = key_search(data, args.search)
            if found:
                data = search_value
                if not args.quiet:
                    path_str = 'search path: {}\n'.format(' '.join(str(x) for x in path))
                    stderr.write(path_str)
            else:
                stderr.write(f"search: key '{args.search}' not found.\n")
        cmd(data)


if __name__ == '__main__':
    main()
