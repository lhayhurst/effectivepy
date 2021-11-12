# often, list comprehensions need to reference the same computation in multiple places
# you can use the walrus operator to remove redundancy
from typing import Callable, Dict, List

import pytest


def get_batches(count: int, size: int) -> int:
    return count // size


def sufficiently_in_stock(orders: List[str], stock: Dict[str, int]) -> Dict[str, int]:
    ret = dict()
    for name in orders:
        count = stock.get(name, 0)
        batches = get_batches(count, 8)
        if batches:
            ret[name] = batches
    return ret


def test_sufficiently_in_stock():
    orders = ["screws", "wingnuts", "clips"]
    stock = {"nails": 125, "screws": 35, "wingnuts": 8, "washers": 24}
    found = sufficiently_in_stock(orders, stock)
    assert found == {"screws": 4, "wingnuts": 1}


# Great. but let's make the sufficiently in stock function use comprehensions.
def sufficiently_in_stock_icky(orders: List[str], stock: Dict[str, int]) -> Dict[str, int]:
    return {name: get_batches(stock.get(name, 0), 8) for name in orders if get_batches(stock.get(name, 0), 8)}


def test_sufficiently_in_stock_icky():
    orders = ["screws", "wingnuts", "clips"]
    stock = {"nails": 125, "screws": 35, "wingnuts": 8, "washers": 24}
    found = sufficiently_in_stock_icky(orders, stock)
    assert found == {"screws": 4, "wingnuts": 1}


# Less code, but annoying duplication. walrus operator to the rescue!
def sufficiently_in_stock_elegant(orders: List[str], stock: Dict[str, int]) -> Dict[str, int]:
    return {name: batches for name in orders if (batches := get_batches(stock.get(name, 0), 8))}


# Much nicer! Let's put in all in one test, because.
@pytest.mark.parametrize("f", [sufficiently_in_stock, sufficiently_in_stock_icky, sufficiently_in_stock_elegant])
def test_in_stock(f: Callable):
    orders = ["screws", "wingnuts", "clips"]
    stock = {"nails": 125, "screws": 35, "wingnuts": 8, "washers": 24}
    assert f(orders, stock) == {"screws": 4, "wingnuts": 1}


# note that, if a comprehension uses the walrus operator in the value part of the comprehension, and
# doesn't have a condition, it'll leak the loop variable into containing scope (remember item 21)
def test_leaky_walrus():
    stock = {"nails": 125, "screws": 35, "wingnuts": 8, "washers": 24}
    half = [(last := count // 2) for count in stock.values()]
    assert half == [62, 17, 4, 12]
    assert last == 12  # noqa F821

    # this leakage is normal for loop variables. consider:
    # for count in stock.values():
    #   pass
    # print(count)  # its 24


# because of this leaky behavior, use the walrus operator only in the expression part of the comprehension
