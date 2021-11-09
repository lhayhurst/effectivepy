# his assertion is that, for single argument functions, list comprehension is clear than map.
# let's test that.


def test_usability_claim_about_list_compr_vs_map():
    # write a func that doubles every argument
    doubled_compr = [x * 2 for x in range(1, 11)]
    doubled_map = map(lambda x: x * 2, range(1, 11))

    assert doubled_compr == list(doubled_map)  # the doubled map is a map object, and must be listified.


def test_usability_claim_about_list_compr_vs_filter():
    # filter out the evens
    list_compr = [x for x in range(1, 11) if x % 2 == 0]
    filtered = filter(lambda x: x % 2 == 0, range(1, 11))
    assert list_compr == list(filtered) == [2, 4, 6, 8, 10]


# debate-able? let's combine the two. square the only the even arguments.


def test_usability_claims_when_given_something_a_double_condition():
    # double the evens
    list_compr = [x ** 2 for x in range(1, 11) if x % 2 == 0]
    tortured = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(1, 11)))
    assert list_compr == list(tortured) == [4, 16, 36, 64, 100]

    # the list comprehension does in fact appear easier to read and maintain


def test_usability_claims_with_dictionaries():
    even_squares_dict = {x: x ** 2 for x in range(1, 11)}
    tortured = dict(map(lambda x: (x, x ** 2), range(1, 11)))
    assert even_squares_dict == tortured == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


def test_usability_claims_with_tests():
    three_cubed_set = {x ** 3 for x in range(1, 11)}
    tortured = set(map(lambda x: x ** 3, range(1, 11)))
    assert three_cubed_set == tortured
