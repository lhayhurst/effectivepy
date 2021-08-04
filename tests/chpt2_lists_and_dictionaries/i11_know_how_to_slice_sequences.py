def test_basic_slicing():
    a = [chr(i) for i in range(97, 105)]  # a-g

    assert a[3:5] == ["d", "e"]  # middle two
    assert a[1:7] == ["b", "c", "d", "e", "f", "g"]  # all but the ends

    # when slicing from beginning of list, you can leave out the 0 to reduce line noise
    assert a[:5] == a[0:5]

    # when slicing to the end of the list, you can leave out the final index because it is redundant
    assert a[5:] == a[5 : len(a)]

    # you can leave them both off too
    assert a[:] == a

    # using negative numbers for slicing is helpful for doing offsets relative to the end of a list
    assert a[:-1] == a[: len(a) - 1]
    assert a[-3:] == a[len(a) - 3 :]
    assert a[2:-1] == a[2 : len(a) - 1]
    assert a[-3:-1] == ["f", "g"]


def test_slicing_creates_copies():
    # slicing a list results in a whole new list
    a = [chr(i) for i in range(97, 105)]  # a-g
    b = a[3:]
    assert id(a) != id(b)
    a[0] = "foo"
    assert b[0] != "foo"

    # if you leave out start and ed, you end up with a copy of the original
    b = a[:]
    assert b == a and b is not a

    # if you assign to a slice with no start or end indexes, you replace the all contents of the list
    # with a copy of what's referenced (instead of allocating a whole new list)
    b = a
    a[:] = [101, 102, 103]
    assert b == [101, 102, 103]
    assert b is a
