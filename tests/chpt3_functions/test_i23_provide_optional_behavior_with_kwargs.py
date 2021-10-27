import pytest


def remainder(number, divisor) -> int:
    return number % divisor


# This don't won't even get passed the top_level_collect step!
# def test_remainder_raises_when_positional_argument_follows_keyword_argument():
#     with pytest.raises(SyntaxError, match="positional argument follows keyword argument"):
#         remainder(number=5, 2)


def test_remainder_raises_when_multiple_values_provided_for_argument():
    with pytest.raises(TypeError, match="got multiple values for argument"):
        remainder(20, number=7)


def test_kwargs_can_be_splatted_in():
    my_kwargs = {"number": 20, "divisor": 7}
    assert remainder(**my_kwargs) == 6

    # you can mix and match
    assert remainder(number=20, **dict(divisor=7)) == 6

    # you can splat more than once if there aren't overlapping keys
    assert remainder(**dict(number=20), **dict(divisor=7)) == 6


def test_kwargs_as_catch_all_param():
    def stringify_params(**kwargs):
        ret = ""
        for key, value in kwargs.items():
            ret += f"{key} = {value};"
        return ret

    assert stringify_params(alpha=1.5, beta=9, gamma=4) == "alpha = 1.5;beta = 9;gamma = 4;"


# benefits of key word arguments
# 1 maintainability: its more readable to people looking at the code the first time
# 2 allows for defaults (could be a bad thing ;-)
# 3 you can extend a functions params while remaining backwards comptabile with existing callers
