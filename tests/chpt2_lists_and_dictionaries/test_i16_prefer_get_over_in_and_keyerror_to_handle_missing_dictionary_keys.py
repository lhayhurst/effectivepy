# fundamental dictionary ops are get, set, and delete
# py dicts are dynaminic so there is no guarantee a key
# will be there when you access or delete it!
import collections


def test_using_in():
    d = {"a": 1}
    assert "a" in d
    assert "b" not in d


def test_using_key_error():
    d = {"a": 1}
    try:
        d["a"]
    except KeyError:
        assert False  # noqa: B011


def test_using_get():
    d = {"a": 1}
    assert d.get("a", 0) == 1  # this is the shortest and simplest way
    assert d.get("b", 0) == 0


def test_get_with_complex_value_type():
    votes = {"baguette": ["Bob", "Alice"], "ciabatta": ["Coco", "Deb"]}

    key = "brioche"
    who = "Elmer"

    if key in votes:
        names = votes[key]
    else:
        votes[key] = names = [who]  # populate the key in one line instead of two

    assert names == ["Elmer"]


def test_using_defaultdict():  # this is the best way to do this!
    votes = collections.defaultdict(list)
    votes["baguette"].append("Bob")
    votes["baguette"].append("Alice")
    assert votes["baguette"] == ["Bob", "Alice"]
