from base64 import decodebytes
from sys import stderr
from typing import Any

from .load_yaml import timestamp_to_datetime


def change_type(key: str, data_type: str) -> Any:
    try:
        if data_type == 'int':
            return int(key), True
        if data_type == 'float':
            return float(key), True
        if data_type == 'bool':
            if key.upper() == 'TRUE':
                return True, True
            if key.upper() == 'FALSE':
                return False, True
        if data_type == 'null':
            return None, True
        if data_type == 'bin':
            ascii_key = key.encode('ascii')
            return decodebytes(ascii_key), True
        if data_type == 'timestamp':
            return timestamp_to_datetime(key), True
        stderr.write(
            f"Type error: key '{key}' could not be converted to type '{data_type}'.\n"
        )
        return key, False
    except Exception:
        stderr.write(
            f"Type error: key '{key}' could not be converted to type '{data_type}'.\n"
        )
        return key, False
