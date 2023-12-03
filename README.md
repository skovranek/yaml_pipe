# YAML\_Pipe
CLI utility for extracting YAML or JSON data.

## Overview
You can use YAML\_Pipe as a CLI utility to access and/or search for the key of specific data nodes in a YAML or JSON file. This may help with data processing by not requiring you to, first, manually open and literally read the data file, then then write code in your program to access certain keys to extract the data, and then run your program. YAML\_Pipe let's you grab the data, and then pipe it as input to another CLI tool or write it to a new file. It does not modify the original file.

## Features
Usage:
```
$ yaml_pipe [-h/--help] [-q/--quiet]
<file> <enumerate, yaml, or json> <keys...>
[--search <key>] [--type <int, float, bool, bin, null, or timestamp>]
```
'yaml\_pipe' takes three positional arguments, and four options. Provides autocomplete and abbreviation.
- HELP: [-h/--help] Usual help option.
- QUIET: [-q/--quiet] Option to turn off success messages printed to stderr.
- FILE: [file] Must include path to data file to parse as YAML (JSON is a subset of YAML).
- COMMAND: \<enumerate, yaml, or json> Must select one of three commands:
  - ENUMERATE: Print the nodes at the current level, no nesting. Index list items.
  - YAML: Output YAML data.
  - JSON: Output JSON data.
- KEYS: \<keys ...> Optionally provide keys and/or indices as extra args to access nested nodes. Tab for autocomplete to list keys and indices.
- SEARCH: [--search \<key>] Optionally search for a key. Must match exactly. Default data type is a string.
- TYPE: [--type \<data\_type>] Optionally select the data type of search keys that are not strings. Each choice correlates with a YAML data tag. Is an option for the search option.
![gif demonstrating autocomplete](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3kwOXVxbTlhZjcyOHl6czk5dzFzbzhudHgyejFld2o3bzYwNnJkdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7Skla52RfNo837pfvN/giphy.gif)
> [!NOTE]
> To ensure autocomplete with argcomplete works as intended, follow the order of arguments found here:
> `$ yaml_pipe -q file command keys... --search key --type data_type`

## Download/Install
From source:
1) Clone the repo:
```
$ git clone https://github.com/skovranek/yaml_pipe
```
2) Change directories to the new 'yaml\_pipe directory/', then run:
```
$ python3 -m pip install -e .
$ eval "$(register-python-argcomplete3 yaml_pipe)"
```

> [!NOTE]
> YAML\_Pipe is not published on Pypi.com. Trying to install with pip will install a different package with a similar name.

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
The main dependencies of YAML\_Pipe are ruamel.yaml to parse YAML and JSON, argparse to parse CLI args, and [argcomplete](https://pypi.org/project/argcomplete/) to autocomplete arguments and options.

View the requirements.txt file for an exhaustive list of dependencies.

## Testing
Manually tested with a zsh shell in the macOS terminal.

## Contact
Questions, issues or suggestions: mattjskov at gmail.com

## Contribute
Anyone is welcome to submit pull requests to the main branch.
