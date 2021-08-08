import pytest


def test_unpack_raises_when_tried_naively():
    car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
    car_ages_descending = sorted(car_ages, reverse=True)

    with pytest.raises(ValueError, match="too many values to unpack"):
        oldest, second_oldest = car_ages_descending


def test_unpack_works_with_starred_expression():
    car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
    car_ages_descending = sorted(car_ages, reverse=True)
    oldest, second_oldest, *the_rest = car_ages_descending

    assert oldest == 20
    assert second_oldest == 19
    assert set(the_rest) == set(car_ages) - {20, 19}

    # starred expressions can appear in any position!
    oldest, *others, youngest = car_ages_descending
    assert oldest == 20
    assert youngest == 0
    assert set(others) == set(others) - {20, 0}

    *others, second_youngest, youngest = car_ages_descending
    assert second_youngest == 1
    assert youngest == 0
    assert set(others) == set(others) - {1, 0}


# the below won't even compile!
# def test_unpack_assignment_raises_when_only_starred_expression_is_used():
#    with pytest.raises(ValueError, match="starred assignment target must be in a list or tuple"):
#        *stuff = list(range(1, 10))


def test_starred_expressions_become_list_instances():
    short_list = [1, 2]
    first, second, *rest = short_list
    assert first == 1
    assert second == 2
    assert rest == []


def test_unpack_arbitary_iterators():
    it = iter(range(1, 4))
    first, second, *rest = it
    assert first == 1
    assert second == 2
    assert rest == [3]
