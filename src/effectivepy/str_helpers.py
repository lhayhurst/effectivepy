from typing import Union


def to_str(bytes_or_str: Union[str, bytes]) -> str:
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode("utf-8")
    elif isinstance(bytes_or_str, str):
        return bytes_or_str
    else:
        raise ValueError(f"Unexpected type: {type(bytes_or_str)}")


def to_bytes(bytes_or_str: Union[str, bytes]) -> bytes:
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode("utf-8")
    elif isinstance(bytes_or_str, bytes):
        return bytes_or_str
    else:
        raise ValueError(f"Unexpected type: {type(bytes_or_str)}")
