# don't do this!
from typing import Union

import pytest


def careful_divide(numerator, denominator) -> Union[None, float]:
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return None


def test_careful_divide():
    assert not careful_divide(1, 0)

    # works fine, but what if the numerator is zero?
    assert not careful_divide(0, 1)

    # this misinterpretation of False-equivilant return value is a common
    # mistake in Python code where None has special meaning.


def better_careful_divide(numerator, denominator) -> float:
    try:
        return numerator / denominator
    except ZeroDivisionError as e:
        raise ValueError(f"Invalid inputs: {numerator} / {denominator} raised {e}")


def test_better_careful_divide():
    with pytest.raises(ValueError):
        better_careful_divide(1, 0)
