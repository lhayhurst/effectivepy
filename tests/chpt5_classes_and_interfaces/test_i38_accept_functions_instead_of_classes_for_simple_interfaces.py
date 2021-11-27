# Many of python's built-in apis allow you to customize behavior with parametrized functions. consider:
from collections import defaultdict


def test_sort_key():
    names = ["Elanour", "Chidi", "Tahani", "Jason", "Michael", "Janet"]
    sorted_names = sorted(names, key=len)
    assert sorted_names == ["Chidi", "Jason", "Janet", "Tahani", "Elanour", "Michael"]


# in other languages, you might expect hooks to be defined by abstract classes
# but in py, hooks are usually stateless functions like len
# they are better because a) easier to define b) simpler c) first class objects


def test_customize_default_dict():
    num_keys_added = 0

    def count_missing():
        nonlocal num_keys_added
        num_keys_added += 1
        return 0

    current = {"green": 12, "blue": 3}
    increments = {"red": 5, "blue": 17, "orange": 9}

    result = defaultdict(count_missing, current)

    for k, v in increments.items():
        result[k] += v

    assert num_keys_added == 2


# the above is gross because the usage of nonlocal.
# the problem with using closures for stateful hooks is that its harder to read
# and use than a stateless function example.
# a better approach is to use a small class that encapsulates the state


def test_better_count_missing():
    class CountMissing:
        def __init__(self):
            self.added = 0

        def missing(self):
            self.added += 1
            return 0

    counter = CountMissing()

    current = {"green": 12, "blue": 3}
    increments = {"red": 5, "blue": 17, "orange": 9}

    result = defaultdict(counter.missing, current)

    for k, v in increments.items():
        result[k] += v

    assert counter.added == 2


# But this could still isn't great. Its not obvious what the purpose of CountMissing is, without context
# Who makes it? Who calls missing? Without peeking into the defaultdict impl, its not clear
# the best solution involves overwriting __call__ in CountMissing, which allows an object to be called
# just like a function


def test_best_count_missing():
    class BestCountMissing:
        def __init__(self):
            self.added = 0

        def __call__(self):
            self.added += 1
            return 0

    counter = BestCountMissing()

    current = {"green": 12, "blue": 3}
    increments = {"red": 5, "blue": 17, "orange": 9}

    result = defaultdict(counter, current)

    for k, v in increments.items():
        result[k] += v

    assert counter.added == 2


# this is way better
# the __call__ method indicates that a classes instances will be called somewhere
# where a function argument would be expected (ie, as an API hook)
# it provides a strong hint that the class is going to be used as a stateful closjure
# best of all, the defaultdict still has no view as to what is going on in __call__.
# all it needs is a function for the default value hook.
