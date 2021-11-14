# list comprehensions are nice for small sequences, but for large inputs, the program could
# consume too much memory and oom
# to solve this, python provides _generator expressions_ (vs list comprehensions). let's try it
import collections
import sys


def test_generator_expression():
    ge = (i for i in range(1, sys.maxsize))
    assert isinstance(ge, collections.Generator)
    assert next(ge) == 1
    assert next(ge) == 2


# another powerful use of generators is that they can be composed together


def test_generator_expression_composition():
    ge1 = (i for i in range(1, 10))
    ge2 = ((i, i ** 2) for i in ge1)

    assert next(ge2) == (1, 1)
    assert next(ge2) == (2, 4)


# when you want to compose functionality that's  operating on a stream of large input,
# composed generator expressions are a great choice! they execute quickly and are memory efficient.
