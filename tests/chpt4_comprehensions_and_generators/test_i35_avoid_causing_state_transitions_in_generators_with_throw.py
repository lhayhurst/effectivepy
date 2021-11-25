# in addition to yield from, and send, another advanced generator feature is the throw menthod for reraising
# exception instances in generator functions.

# the way it works is simple: when the method is called, the next occurance of a yield expression
# reraises the provided Exception instance after its output is received, instead of continuing normally
import pytest


class MyError(Exception):
    pass


def test_it():
    def my_generator():
        yield 1
        yield 2
        yield 3

    it = my_generator()
    assert next(it) == 1
    assert next(it) == 2
    with pytest.raises(MyError):
        it.throw(MyError("test error"))


# when you call throw, the generator function may catch the injection exception with a standard try/catch


def test_catching_exception_in_generator(capsys):
    def my_generator():
        yield 1
        try:
            yield 2
        except MyError:
            print("Got MyError")
        else:
            yield 3
        yield 4

    iter = my_generator()
    assert next(iter) == 1
    assert next(iter) == 2
    iter.throw(MyError("test error"))
    assert "Got MyError" in capsys.readouterr().out


# this provides a form of 2-way communication channel between the generator and the caller at
# the position of the most recently excecuted yield expression

# it harms readability because it requires additional nesting and boilerpate in order to raise and
# catch exceptions

# a better way to provide exceptional behavior with generators is to use a class that implements the
# __iter__ method along with methods that cause exceptional state transitions
