def test_simple_example():
    def sort_priority(values, group):
        def helper(x):
            if x in group:
                return (0, x)
            return (1, x)

        values.sort(key=helper)

    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    sort_priority(numbers, group)
    assert numbers == [2, 3, 5, 7, 1, 4, 6, 8]


# This function works because:
# 1 Python supports _closures_: functions that refer to variables from the scope
#   in which they were defined. Helper, here, knows about group.
# 2 Functions are first class objects in Python. You can make variables out of them,
#   refer to them directly.

# The "scoping bug", which bites n00bs,
# prevents local variables from polluting the containing module's namespace.
def test_scoping_bug_behaves_as_expected():
    baz = False

    def foo():
        baz = True  # noqa: F841

    foo()
    assert not baz


# avoid doing this for anything but simple things.
def test_scoping_bug_using_non_local():
    baz = False

    def foo():
        nonlocal baz
        baz = True

    foo()
    assert baz
