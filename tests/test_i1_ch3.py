from typing import Union


def test_byte_contain_raw_unsigned_8_bit_values():
    a = b"h\x65llo"
    assert list(a) == [ord("h"), ord("e"), ord("l"), ord("l"), ord("o")]


def test_strings_contain_code_points():
    a = "a\u0300 propos"
    assert list(a) == ["a", "̀", " ", "p", "r", "o", "p", "o", "s"]


def test_unicode_sandwich():
    def to_str(bytes_or_str: Union[str, bytes]) -> str:
        if isinstance(bytes_or_str, bytes):
            return bytes_or_str.decode("utf-8")
        elif isinstance(bytes_or_str, str):
            return bytes_or_str
        else:
            raise ValueError(f"Unexpected type: {type(bytes_or_str)}")

    assert "foo" == to_str("foo")
    assert "bar" == to_str(b"bar")

    def to_bytes(bytes_or_str: Union[str, bytes]) -> bytes:
        if isinstance(bytes_or_str, str):
            return bytes_or_str.encode("utf-8")
        elif isinstance(bytes_or_str, bytes):
            return bytes_or_str
        else:
            raise ValueError(f"Unexpected type: {type(bytes_or_str)}")

    assert b"foo" == to_bytes("foo")
    assert b"bar" == to_bytes(b"bar")
