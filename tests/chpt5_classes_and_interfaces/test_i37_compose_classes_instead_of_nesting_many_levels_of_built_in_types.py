# Python's built in dictionary and tuple types make it easy to keep track of dynamic state
# but avoid managing internal state if you are doing more than one level of internal nesting
# using dicts inside dicts inside ... makes your code hard to read, and hard to maintain

# when the bookkeeping gets overcomplicated, break it into classes.
# you can then provide well defined interfaces that better encapsulate your data
# this also allows you to create a layer of abstraction between your interface, and your concrete impls.

from collections import namedtuple


# named tuples have two limitations:
# 1 you don't get default argument values. could be a good thing ;-)
# 2 the attribute values of the namedtuple instance is accessible by the client using
# numerical indexes and enumerations. this can create bad coupling between client and library code.
# if you aren't in control of the client usages, better to use an actual class

Grade = namedtuple("Grade", ("score", "weight"))


def test_demonstrate_named_tuple_issues():
    g = Grade(95, 1.2)
    assert g[0] == 95  # gross
    assert g[1] == 1.2  # gross
    assert list(g) == [95, 1.2]  # gross
