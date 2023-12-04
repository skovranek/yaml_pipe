# YAML\_Pipe (PyPI: pipeyaml)
CLI utility for extracting YAML or JSON data.

## Overview
You can use YAML\_Pipe as a CLI utility to access and/or search for the key of specific data nodes in a YAML or JSON file. This may help with data processing by not requiring you to, first, manually open and literally read the data file, then then write code in your program to access certain keys to extract the data, and then run your program. YAML\_Pipe let's you grab the data, and then pipe it as input to another CLI tool or write it to a new file. It does not modify the original file.

## Features
![gif demonstrating autocomplete](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3kwOXVxbTlhZjcyOHl6czk5dzFzbzhudHgyejFld2o3bzYwNnJkdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7Skla52RfNo837pfvN/giphy.gif)

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
  - ENUMERATE: Print the nodes at the current level. No nesting. Index sequences.
  - YAML: Output YAML data.
  - JSON: Output JSON string.
- KEYS: \<keys ...> Optionally provide keys and/or indices as extra args to access nested nodes. Tab for autocomplete to list keys and indices.
- SEARCH: [--search \<key>] Optionally search for a key. Must match exactly. Default data type is a string.
- TYPE: [--type \<data\_type>] Optionally select the data type of search keys that are not strings. Each choice correlates with a YAML data tag. Is an option for the search option.
> [!NOTE]
> To ensure autocomplete with argcomplete works as intended, follow the order of arguments found here:
> `$ yaml_pipe -q file command keys... --search key --type data_type`

## Download/Install
From source:
1) Clone this repo:
```
$ git clone https://github.com/skovranek/yaml_pipe
```
2) Change directories to the new 'yaml\_pipe directory/', then run:
```
$ python3 -m pip install -e .
$ eval "$(register-python-argcomplete3 yaml_pipe)"
```
From PyPI:
```
$ pip install pipeyaml
```
> [!NOTE]
> YAML\_Pipe is published on PyPI as 'pipeyaml', not 'yaml\_pipe' or 'yamlpipe'.

## Implement Library
There are a few different functions from this project you may want to import.
> access\_keys(node: Any, keys: List[str]) -> Any, bool:

Attempt to access value in a series of nested dicts and lists via list of keys and indices as strings. True/False for exists/not exists.

> key\_search(node: Any, key: str) -> Any, List[Any], bool:

Attempt to find dict key in series of nested dicts and lists. Returned list is path of keys or indices to access value. True/False for found/not found.

> print\_keys(node: Any):

Prints the first layer of nodes. Keys are listed. Sequences are indexed. Nested values are printed inline flow style.

View the [main](hhhttps://github.com/skovranek/yaml_pipe/blob/main/requirements.txt) function of Yaml\_Pip for an example of how these functions are used.
## Dependencies
The main dependencies of YAML\_Pipe are [ruamel.yaml](https://pypi.org/project/ruamel.yaml/) to parse YAML and JSON, [argparse](https://docs.python.org/3/library/argparse.html) to parse CLI args, and [argcomplete](https://pypi.org/project/argcomplete/) to autocomplete arguments and options.

View the [requirements.txt](https://github.com/skovranek/yaml_pipe/blob/main/requirements.txt) file for the entire list of dependencies.

## Testing
Manually tested with a zsh shell in the macOS terminal.

## Contact
Questions, issues or suggestions: mattjskov at gmail.com

## Contribute
Anyone is welcome to submit pull requests to the main branch.
