# YAML\_Pipe
CLI utility for extracting YAML or JSON data.

## Overview
You can use YAML\_Pipe as a CLI utility to access and/or search for the key of specific data nodes in a YAML or JSON file. This may help with data processing by not requiring you to, first, manually open and literally read the data file, then then write code in your program to access certain keys to extract the data, and then run your program. YAML\_Pipe let's you grab the data, and then pipe it as input to another CLI tool or write it to a new file. It does not modify the original file.

## Features
Usage:
```
$ yaml_pipe [-h/--help] [-q/--quiet] <file> <enumerate, yaml, json, or print>
[--search <key>] [--type <int, float, bool, bin, null, or timestamp>]
<keys...>
```
'yaml\_pipe' takes three positional arguments, and four options. Provides autocomplete and abbreviation.
- HELP: [-h/--help] Usual help option.
- QUIET: [-q/--quiet] Option to turn off success messages printed to stderr.
- FILE: [file] Must include path to data file to parse as YAML (JSON is a subset of YAML).
- COMMAND: \<enumerate, yaml, or json> Must select one of three commands:
  - ENUMERATE: List only the nodes at the current level, no nesting.
  - YAML: Output YAML data.
  - JSON: Output JSON data.
  - PRINT: Prints YAML with additional annotations for navigability.
- SEARCH: [--search \<key>] Optionally search for a key. Must match exactly. Default data type is a string.
- TYPE: [--type \<data\_type>] Optionally select data type of search keys that are not strings. Each choice correlates with a YAML data tag. Must use with search option.
- KEYS: \<keys ...> Optionally provide keys and/or indices as extra args to access nested nodes. Tab for autocomplete to list keys and indices.

## Download/Install
Run
```
$ python3 -m pip install yaml_pipe
$ eval "$(register-python-argcomplete yaml_pipe)"
```
## Implement Library
There are a few different functions from this project you may want to import.
> access\_keys(node: Any, keys: List[str]) -> Any, bool:

Attempt to access value in a series of nested dicts and lists via list of keys and indices as strings. True/False for exists/not exists.

> key\_search(node: Any, key: str) -> Any, List[Any], bool:

Attempt to find dict key in series of nested dicts and lists. Returned list is path of keys or indices to access value. True/False for found/not found.

> print\_keys(node: Any):

Prints the first layer of nodes. It lists the elements of a list or keys of a dict. Nested values are printed inline flow style.

Here is the main function of Yaml\_Pip to demonstrate how these functions are used.

```py
def main():
    args = parse()
    data = load(args.data)
    if args.cmd in COMMANDS:
        cmd = COMMANDS[args.cmd]
        if len(args.keys) > 0:
            nested_node, exists = access_keys(data, args.keys)
            if exists:
                data = nested_node
            if not args.quiet:
                write(f"keys success: {exists}.\n")
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
                    write(path_str)
            else:
                write(f"search: key '{args.search}' not found.\n")
        cmd(data)
```

## Dependencies
The main dependencies of YAML\_Pipe are ruamel.yaml to parse YAML and JSON, argparse to parse CLI args, and argcomplete to autocomplete arguments and options.

View the requirements.txt file for an exhaustive list of dependencies.

## Testing
Manually tested with a zsh shell in the macOS terminal.

## Contact
Questions, issues or suggestions: mattjskov at gmail.com

## Contribute
Anyone is welcome to submit pull requests to the main branch.
