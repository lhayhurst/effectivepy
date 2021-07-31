import itertools

import pytest


def test_basic_case():
    names = ["gandalf", "frodo", "aragorn"]
    weapons = ["staff", "short sword", "sword"]

    results = zip(names, weapons)
    assert next(results) == ("gandalf", "staff")
    assert next(results) == ("frodo", "short sword")
    assert next(results) == ("aragorn", "sword")


def test_truncating_case():
    names = ["gandalf", "frodo", "aragorn"]
    weapons = ["staff", "short sword"]

    results = zip(names, weapons)
    assert next(results) == ("gandalf", "staff")
    assert next(results) == ("frodo", "short sword")

    with pytest.raises(StopIteration):
        next(results)


def test_truncating_case_with_zip_longest():
    names = ["gandalf", "frodo", "aragorn"]
    weapons = ["staff", "short sword"]

    results = itertools.zip_longest(names, weapons)
    assert next(results) == ("gandalf", "staff")
    assert next(results) == ("frodo", "short sword")
    assert next(results) == ("aragorn", None)
