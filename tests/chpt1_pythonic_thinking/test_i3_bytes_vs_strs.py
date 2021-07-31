import locale

import pytest


from effectivepy.str_helpers import to_bytes, to_str


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


def test_writing_bytes_with_python2_behavior_raises(tmp_path):
    with pytest.raises(TypeError):
        with tmp_path.open("data.bin", "w") as f:
            f.write(b"Not gonna work here anymore")


def test_reading_bytes_with_python2_behavior_raises(tmp_path):
    bin_file = tmp_path / "data.bin"
    bin_file.write_bytes(b"\xf1\xf2\xf3\xf4\xf5")

    with pytest.raises(UnicodeDecodeError):
        with bin_file.open("r") as f:
            _ = f.read()

    # but you can read it in as a legacy windows encoding
    with bin_file.open("r", encoding="cp1252") as f:
        assert f.read() == "ñòóôõ"


def test_can_verify_locale():
    assert locale.getpreferredencoding() == "UTF-8"
