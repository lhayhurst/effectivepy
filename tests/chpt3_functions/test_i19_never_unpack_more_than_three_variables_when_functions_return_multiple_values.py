# this recipe is fairly simple, in that it describes weird bugs that
# can emerge if you unpack a whole bunch of values from a function.
# these bugs are related to the tight binding that emerges between
# the caller and the call site.
# the recommended refactoring is to return a class or namedtuple.
def test_multiple_return_values():
    def foo():
        return "foo", "bar"

    f, b = foo()
    assert f == "foo"
    assert b == "bar"
