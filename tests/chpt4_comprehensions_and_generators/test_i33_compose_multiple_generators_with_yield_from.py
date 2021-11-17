# python has an additional variant on its yield syntax, 'yield from'
# this can be used when you have several levels of yielding (ie from a loop)
import timeit


def child():
    for i in range(100_000):
        yield i


def slow_parent():
    for i in child():
        yield i


def fast_parent():
    yield from child()


def test_slow_versus_fast():
    baseline = timeit.timeit(stmt="for _ in slow_parent(): pass", globals=globals(), number=50)
    comparison = timeit.timeit(stmt="for _ in fast_parent(): pass", globals=globals(), number=50)

    assert comparison < baseline
