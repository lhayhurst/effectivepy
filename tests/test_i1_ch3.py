from effectivepy.str_helpers import to_bytes, to_str

import pytest


def test_byte_contain_raw_unsigned_8_bit_values():
    a = b"h\x65llo"
    assert list(a) == [ord("h"), ord("e"), ord("l"), ord("l"), ord("o")]


def test_strings_contain_code_points():
    a = "a\u0300 propos"
    assert list(a) == ["a", "̀", " ", "p", "r", "o", "p", "o", "s"]


def test_unicode_sandwich():
    assert "foo" == to_str("foo")
    assert "bar" == to_str(b"bar")

    assert b"foo" == to_bytes("foo")
    assert b"bar" == to_bytes(b"bar")


def test_bad_arg_to_str_helpers_raise():
    with pytest.raises(ValueError):
        to_str(1)

    with pytest.raises(ValueError):
        to_bytes(1)


def test_mixing_up_strs_and_bytes_raises():
    with pytest.raises(TypeError):
        _ = "foo" + b"bar"

    with pytest.raises(TypeError):
        _ = b"foo" + "bar"

    with pytest.raises(TypeError):
        assert "red" > b"blue"

    with pytest.raises(TypeError):
        assert b"red" < "blue"

    with pytest.raises(TypeError):
        b"red %s" % "blue"


def test_bytes_and_strs_are_not_comparable():
    assert "foo" != b"foo"
