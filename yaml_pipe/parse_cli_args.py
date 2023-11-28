'''Module providing a function parsing arguments from CLI.'''
from argparse import Namespace, ArgumentParser
import argcomplete

from .populate_keys import populate_keys


def parse() -> Namespace:
    '''Returns object with key-values from CLI args.'''
    parser = ArgumentParser(
        prog='YAML_Pipe',
        description='Access YAML data in the CLI.',
        epilog='YAML_Pipe created by Matt Skovranek.'
    )

    parser.add_argument(
        'file',
        help='specify path to YAML (or JSON) file',
    ).completer = argcomplete.DirectoriesCompleter

    parser.add_argument(
        'cmd',
        choices=[
            'enumerate',
            'yaml',
            'json',
            'print'
        ],
        help='select command for operating on input data',
    )

    parser.add_argument(
        '-q',
        '--quiet',
        action='store_true',
        help='turn off success messages'
    )
    parser.add_argument(
        '--search',
        metavar='key',
        help='optionally search for specified key'
    )
    parser.add_argument(
        '--type',
        choices=[
            'int',
            'float',
            'bool',
            'null',
            'bin',
            'timestamp'
        ],
        help='optionally select alternate data type of search key',
    )
    parser.add_argument(
        'keys',
        nargs='*',
        help='optionally list keys and indices for accessing nested values'
    ).completer = populate_keys

    argcomplete.autocomplete(parser)
    return parser.parse_args()
