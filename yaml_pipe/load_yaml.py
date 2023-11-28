"""Module providing a function loading YAML."""
from datetime import datetime
from sys import stdout
from typing import Any, Dict

from ruamel.yaml import YAML


# ruamel docs show Any type used for 'data' object
def load(yaml_file: str) -> Dict:
    """Returns data from YAML file."""
    with open(yaml_file, 'r', encoding="utf-8") as yaml_data:
        yaml = YAML(typ="safe", pure=True)
        data = yaml.load(yaml_data)
    return data


def dump(node: Any):
    """writes object to stdout"""
    yaml=YAML()
    yaml.default_flow_style = False
    yaml.dump(node, stdout)


def timestamp_to_datetime(timestamp: str) -> datetime:
    yaml=YAML(typ="safe", pure=True)
    data = yaml.load(
f"""
---
datetime: !!timestamp {timestamp}
...
""")
    return data['datetime']
