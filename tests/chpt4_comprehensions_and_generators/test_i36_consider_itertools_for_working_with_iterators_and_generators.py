import itertools

# iteratools functions fall into three main categories:
# 1 linking things together => chain, repeat, cycle, tee, zip_longest
# 2 filtering items => islice, takewhile, dropwhile, filterfalse
# 3 producing combinations of items => accumulate, product, permutations, combinations, combinations_with_replacement


def test_chain():
    # use chain to combine multiple iterators together
    a = range(1, 11)
    b = range(11, 21)
    c = itertools.chain(a, b)
    assert list(c) == list(range(1, 21))


def test_repeat():
    # use repeat to output a single value forever,
    # or use the second parameter to specify a maximum number of times
    it = itertools.repeat("Hello", 3)
    assert list(it) == ["Hello", "Hello", "Hello"]


def test_cycle():
    # use cycle to repeat an iterator's items forever
    it = itertools.cycle([1, 2])
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 1


def test_tee():
    # use tee to split a single iterator into the number of parallel iterators specified
    # by the second parameter. the memory usage of this function will grow if the iterators
    # do not progress at the same speed, since buffering is needed to enqueue the pending items
    input_list = ["a", "b"]
    it1, it2, it3 = itertools.tee(input_list, 3)
    assert list(it1) == input_list
    assert list(it2) == input_list
    assert list(it3) == input_list


def test_zip_longest():
    # a variant of the built-in zip; it returns a placeholder value when an iterator is exhausted,
    # which can happen when the lists are of different lengths
    keys = ["one", "two", "three"]
    values = [1, 2]

    normal = zip(keys, values)
    assert list(normal) == [("one", 1), ("two", 2)]

    longest = itertools.zip_longest(keys, values)
    assert list(longest) == [("one", 1), ("two", 2), ("three", None)]

    # zip_longest has a fill value that you can use!
    longest = itertools.zip_longest(keys, values, fillvalue=3)
    assert list(longest) == [("one", 1), ("two", 2), ("three", 3)]


# Itertools has a number of functions for filtering items from an iterator
# These include islice, takewhile, dropwhile, and filterfalse


def test_islice():
    # use islice to slice an iterator by numerical indices without copying.
    values = list(range(1, 11))

    first_five = itertools.islice(values, 5)
    assert list(first_five) == list(range(1, 6))

    middle_odds = itertools.islice(values, 2, 8, 2)  # starting at location 2, ending at 8, hopping in incr of 2
    assert list(middle_odds) == [3, 5, 7]


def test_takewhile():
    # takewhile returns items from an iterator until a predicate function returns false for an item
    values = range(1, 10)
    it = itertools.takewhile(lambda x: x < 7, values)
    assert list(it) == list(range(1, 7))


def test_dropwhile():
    # dropwhile is the opposite of takewhile. it skips items until the predicate function is true
    values = range(1, 10)
    it = itertools.dropwhile(lambda x: x < 7, values)
    assert list(it) == list(range(7, 10))


def test_filterfalse():
    # filterfalse is the opposite of the built-in filter fucntion: it returns all items where the pred is false
    values = range(1, 11)
    it1, it2 = itertools.tee(values, 2)
    assert list(itertools.filterfalse(lambda x: x % 2 == 0, it1)) == [1, 3, 5, 7, 9]
    assert list(filter(lambda x: x % 2 == 0, it2)) == [2, 4, 6, 8, 10]


# Itertools also features some functions for producing combinations


def test_accumulate():
    # accumulate folds an item from an iterator into a running value by applying a function that
    # takes two parameters. It outputs the accumulated result for each input value.
    values = [1, 2, 3]
    sum_reduce = itertools.accumulate(values)  # the default function is sum
    assert list(sum_reduce) == [1, 3, 6]  # 1, then 1 + 2, then 1 + 2 + 3

    # let's try it with our own custom binary function
    def sum_modulo_2(first: int, second: int) -> int:
        output = first + second
        return output % 2

    values = [1, 2, 3, 4]
    assert list(itertools.accumulate(values, sum_modulo_2)) == [1, 1, 0, 0]


def test_product():
    # product returns the cartesian product of items from one or more iterators
    assert list(itertools.product([1, 2], repeat=1)) == [(1,), (2,)]
    assert list(itertools.product([1, 2], repeat=2)) == [(1, 1), (1, 2), (2, 1), (2, 2)]
    assert list(itertools.product([1, 2], repeat=3)) == [
        (1, 1, 1),
        (1, 1, 2),
        (1, 2, 1),
        (1, 2, 2),
        (2, 1, 1),
        (2, 1, 2),
        (2, 2, 1),
        (2, 2, 2),
    ]


def test_permutations():
    # permutations returns the unique ordered permutations of length N with items from an iterator
    assert list(itertools.permutations([1, 2], 2)) == [(1, 2), (2, 1)]
    assert list(itertools.permutations([1, 2], 3)) == []  # because 3 > the number of unique items in the input, 2
    assert list(itertools.permutations([1, 2, 3], 2)) == [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    assert list(itertools.permutations([1, 2, 3], 3)) == [
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1),
    ]


def test_combinations():
    # combinations returns the unordered combinations of length N with unrepeated items from an iterator
    assert list(itertools.combinations([1, 2], 1)) == [(1,), (2,)]
    assert list(itertools.combinations([1, 2], 2)) == [(1, 2)]
    assert list(itertools.combinations([1, 2, 3], 2)) == [(1, 2), (1, 3), (2, 3)]


def test_combinations_with_replacement():
    # same as combinations, but repeated values are allowed
    assert list(itertools.combinations_with_replacement([1, 2, 3], 2)) == [
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 2),
        (2, 3),
        (3, 3),
    ]
