import pytest


def safe_division(
    number: int, divisor: int, ignore_overflow: bool, ignore_zero_division: bool
) -> float:
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float("inf")
        else:
            raise


def test_safe_division():
    result = safe_division(1, 10 ** 500, True, False)
    assert result == 0

    with pytest.raises(ZeroDivisionError):
        safe_division(1, 0, False, False)


# The problem is that its easy to confuse the position of the two boleans that control the exceptions.
# One way to improve this is to use optional key word arguments.
# The problem is, because they are optional, there's not way to force callers to use them for clarity.
# You can use _keyword-only_ arguments here.


def better_safe_division(
    number: int, divisor: int, *, ignore_overflow=False, ignore_zero_division=False
):
    return safe_division(number, divisor, ignore_overflow, ignore_zero_division)


# Now the following invocation will result in a TypeError
# better_safe_division(1, 0, False, True)
# "takes 2 positional arguments but 4 were given"

# However, a problem still exists: callers can specify the first two positional arguments
# as positional or keywords. this will create issues if the function author ever decides
# to rename those arguments: because they are named, they are part of the explicit interface.

# Python 3.8 introduces _positional_only_ arguments to solve this issue. You use a "/" to
# indicate the demarking line between the positional and the keyword args.


def even_better_safe_division(
    numerator: int, denominator: int, /, *, ignore_overflow=False, ignore_zero_division=False
):
    return safe_division(numerator, denominator, ignore_overflow, ignore_zero_division)


# note that, if you have paramemters between the / and *,
# they can be passed by position or keyword. tricky.
