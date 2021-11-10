# rule of thumb: avoid using more than two control subexpressions in a comprehension. this could be two conditions,
# two loops, or a condition and a loop. if its more than that, consider using if/foor statements
# and a helper function!


from typing import List


# simple example of subexpressions that isn't bad
def flatten(lols: List[List]) -> List:
    return [list_item for sublist in lols for list_item in sublist]


def test_flatten():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_flatten_lolols():  # flatten list of lists of lists
    def f(lolols):
        return [li for sublist1 in lolols for sublist2 in sublist1 for li in sublist2]  # gross

    assert f([[[1, 2]]]) == [1, 2]


def test_ergo_of_multiple_if_conditions():
    def filter_even_numbers_gt_4(input_list: List[int]) -> List[int]:
        return [x for x in input_list if x > 4 and x % 2 == 0]  # this is fine

    assert filter_even_numbers_gt_4([2, 4, 6, 7, 8, 9, 10]) == [6, 8, 10]

    def filter_matrix_where_cells_are_divisible_by_three_in_rows_that_sum_to_ten_or_higher(matrix):
        return [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]  # this is just gross

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    exp = [[6], [9]]
    assert filter_matrix_where_cells_are_divisible_by_three_in_rows_that_sum_to_ten_or_higher(matrix) == exp
