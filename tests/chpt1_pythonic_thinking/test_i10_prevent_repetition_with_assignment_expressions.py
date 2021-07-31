import pytest


class OutOfStockException(Exception):
    pass


def make_juice_pre_assignment_expr(all_fruit: dict, requested_fruit: str) -> str:
    count = all_fruit.get(requested_fruit, 0)
    if count == 0:
        raise OutOfStockException(requested_fruit)
    return f"{requested_fruit}({count}) juice"


def test_make_juice_pre_assignment_expr():
    fresh_fruit = {"apple": 10, "banana": 8, "lemon": 5, "mango": 0}
    assert make_juice_pre_assignment_expr(fresh_fruit, "lemon") == "lemon(5) juice"

    with pytest.raises(OutOfStockException):
        make_juice_pre_assignment_expr(fresh_fruit, "mango")


def make_juice_with_assignment_expr(all_fruit: dict, requested_fruit: str) -> str:
    if count := all_fruit.get(requested_fruit, 0):
        return f"{requested_fruit}({count}) juice"
    raise OutOfStockException(requested_fruit)


def test_make_juice_with_assignment_expr():
    fresh_fruit = {"apple": 10, "banana": 8, "lemon": 5, "mango": 0}
    assert make_juice_with_assignment_expr(fresh_fruit, "lemon") == "lemon(5) juice"

    with pytest.raises(OutOfStockException):
        make_juice_pre_assignment_expr(fresh_fruit, "mango")
