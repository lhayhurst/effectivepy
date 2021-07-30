def test_dict_as_tuple():
    d = {"foo": 1, "bar": 2, "baz": 3}
    items = tuple(d.items())
    assert items == (("foo", 1), ("bar", 2), ("baz", 3))


def test_unpacking():
    items = ("peanut", "butter")
    p, b = items
    assert p == "peanut"
    assert b == "butter"
