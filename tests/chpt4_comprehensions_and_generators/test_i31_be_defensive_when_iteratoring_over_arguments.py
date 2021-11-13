# its common to iterate over a functions list of arguments multiple times. consider:
from typing import List

import pytest


def normalize_numbers(numbers) -> List[float]:
    total = sum(numbers)
    results = []
    for value in numbers:
        pct = 100 * value / total
        results.append(pct)
    return results


def test_normalize_numbers():
    numbers = [5, 5, 10]
    assert normalize_numbers(numbers) == [25.0, 25.0, 50.0]
    assert sum(normalize_numbers(numbers)) == 100.0


# great. but what if the source of the numbers were a function that yields iterators?
def test_normalize_numbers_with_yielding_function():
    def get_numbers():
        yield 5
        yield 5
        yield 10

    # you get an empty list back because the iterator is exhausted by the first sum() in the normalize numbers method!
    assert normalize_numbers(get_numbers()) == []


# There aren't a lot of great solutions here
# The best solution is, if you are a function and need to loop over the input more than once, to
# a) make a copy of it it (which could be prohibitively expensive) or
# b) raise an exception if you were passed an iterator


def normalize_numbers_safe(numbers) -> List[float]:
    if iter(numbers) == numbers:
        # its an iterable.
        raise TypeError("Must supply a container, got an iteratable")

    total = sum(numbers)
    results = []
    for value in numbers:
        pct = 100 * value / total
        results.append(pct)
    return results


def test_normalize_numbers_safe():
    numbers = [5, 5, 10]
    assert normalize_numbers_safe(numbers) == [25.0, 25.0, 50.0]
    assert sum(normalize_numbers_safe(numbers)) == 100.0


def test_normalize_numbers_safe_raises_when_given_iterable():
    def get_numbers():
        yield 5
        yield 5
        yield 10

    with pytest.raises(TypeError):
        normalize_numbers_safe(get_numbers())
