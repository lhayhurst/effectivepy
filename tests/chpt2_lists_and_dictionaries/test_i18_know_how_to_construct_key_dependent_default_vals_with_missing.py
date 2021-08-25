from collections import defaultdict
from pathlib import Path
from typing import BinaryIO


def open_picture(profile_path):
    try:
        return open(profile_path, "a+b")
    except OSError:
        print(f"Failed to open path {profile_path}")
        raise


class Pictures(dict):
    def __init__(self):
        super().__init__()
        self.times_missing_called = defaultdict(int)

    def __missing__(self, profile_path: str) -> BinaryIO:
        value = open_picture(profile_path)
        self[profile_path] = value
        self.times_missing_called[profile_path] += 1
        return value


def test_missing_impl(tmp_path):
    my_profile_pic: Path = tmp_path / "foo.png"
    my_profile_pic.touch()
    data = b"notreallyimgdata"
    my_profile_pic.write_bytes(data)

    pictures = Pictures()
    handle = pictures[str(my_profile_pic)]  # this will call the missing method!
    assert pictures.times_missing_called[str(my_profile_pic)] == 1

    handle.seek(0)
    image_data = handle.read()
    assert image_data == data

    _ = pictures[str(my_profile_pic)]  # this will call the missing method!
    assert pictures.times_missing_called[str(my_profile_pic)] == 1
