import pytest


def test_simple_stride():
    a = ["red", "orange", "yellow", "green", "blue", "purple"]
    odds = a[::2]  # starting at zero, every second one
    assert odds == ["red", "yellow", "blue"]
    events = a[1::2]
    assert events == ["orange", "green", "purple"]


def test_negative_one_stride_string_reversal_trick():
    x = b"mongoose"
    r = x[::-1]
    assert r == b"esoognom"


# the reversal trick will raise when the string is encoded as a utf-8 byte string
def test_reversal_trick_raises_when_unicode_is_encoded_as_utf8_byte_string():
    w = "语言处理"
    x = w.encode("utf-8")
    y = x[::-1]
    with pytest.raises(UnicodeDecodeError):
        y.decode("utf-8")
