# "Using unpacking wisely will enable you to avoid list indexing when possible, resulting
# in clearer and more Pythonic code."


def test_dict_as_tuple():
    d = {"foo": 1, "bar": 2, "baz": 3}
    items = tuple(d.items())
    assert items == (("foo", 1), ("bar", 2), ("baz", 3))


def test_unpacking():
    items = ("peanut", "butter")
    p, b = items
    assert p == "peanut"
    assert b == "butter"


def test_in_place_swap():
    a = [1, 2, 3, 4]
    a[0], a[1] = a[1], a[0]
    assert a == [2, 1, 3, 4]
