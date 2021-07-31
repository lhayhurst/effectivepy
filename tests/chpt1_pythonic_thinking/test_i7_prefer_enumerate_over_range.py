import pytest


def test_simple_range():
    r = range(0, 2)
    assert isinstance(r, range)
    r = list(r)
    assert len(r) == 2
    assert r == [0, 1]


def test_simple_enumerate():
    r = enumerate(range(0, 2))
    assert isinstance(r, enumerate)
    assert next(r) == (0, 0)
    assert next(r) == (1, 1)

    with pytest.raises(StopIteration):
        next(r)


def test_enumerate_with_custom_start_value():
    r = enumerate(range(0, 2), 100)
    assert list(r) == [(100, 0), (101, 1)]
