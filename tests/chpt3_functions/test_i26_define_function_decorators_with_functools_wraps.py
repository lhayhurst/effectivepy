# Python has decorators!
# Decorators run additional code before and after each call to a function
# They have access to the functions inputs, outputs, and exceptions
# This is useful for enforcing semantics (say, logging functiong), registering functions,
# debugging, etc

# here's a nice thing that can trace all the arguments and return values of a func call
import pickle  # nosec
from functools import wraps

import pytest


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args!r}, {kwargs!r} -> {result!r}")
        return result

    return wrapper


def test_trace(capsys):
    @trace
    def fib(n):
        if n in (0, 1):
            return n
        return fib(n - 2) + fib(n - 1)

    result = fib(4)
    assert result == 3

    output = capsys.readouterr()
    assert "fib((1,), {} -> 1\n" in output.out
    assert "fib((1,), {} -> 3\n"
    assert len(str(output.out).split("\n")) == 10


# This works, but it has a side effect: the wrapped function loses its name!
# It is now called 'wrapper'. Doh.
def test_traced_function_loses_name():
    @trace
    def foo(*args, **kargs):
        pass

    assert foo.__name__ == "wrapper"


# And you can't pickle it either
def foo():
    """ foo """
    pass


@trace
def bar():
    pass


def test_lost_ability_to_pickle_function():
    assert pickle.loads(pickle.dumps(foo)) == foo  # this works fine, but what if you wrap it?

    with pytest.raises(AttributeError, match="Can't pickle local object"):
        pickle.dumps(bar)  # this works fine, but what if you wrap it?


def test_undecorated_function_can_be_helped(capsys):
    help(foo)
    assert "Help on function foo" in capsys.readouterr().out


def test_decorated_function_cannot_be_helped(capsys):
    help(bar)
    assert "Help on function wrapper" in capsys.readouterr().out


# To recap: name gets lost, you lose help, you lose pickling. functools.wraps to the rescue!
# The open source library wrapt is more comprehensive fwiw!


def better_trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args!r}, {kwargs!r} -> {result!r}")
        return result

    return wrapper


@better_trace
def divide(numerator: int, denominator: int, /, *, allow_divide_by_zero=False) -> float:
    """ This is the divide function. """
    if denominator == 0 and not allow_divide_by_zero:
        raise ValueError("Zero demoninator provided")
    return numerator / denominator


def test_better_trace_retains_name():
    assert divide.__name__ == "divide"


def test_better_trace_can_be_pickled():
    assert pickle.loads(pickle.dumps(divide)) == divide


def assert_better_trace_is_helpable(capsys):
    help(better_trace)
    assert "This is the divide function" in capsys.readouterr().out
