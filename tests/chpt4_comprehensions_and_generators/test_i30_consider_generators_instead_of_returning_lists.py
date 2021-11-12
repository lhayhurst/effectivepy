from typing import List


def index_words(text: str) -> List[int]:
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == " ":
            result.append(index + 1)
    return result


def test_index_words():
    address = "Four score and seven years ago..."
    assert index_words(address) == [0, 5, 11, 15, 21, 27]


# Two problems here
# 1) The code is dense and noisy. Append gets called twice.
# 2) There is one line for declaring the list and one for appending to it
# 3) It has 130 characters (w/out whitespace), but only 75 of them really matter

# Better way to do it: with a generator.


def index_words_gen(text: str):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


def test_index_words_gen():
    address = "Four score and seven years ago..."
    assert list(index_words_gen(address)) == [0, 5, 11, 15, 21, 27]


# Nice! The only gotcha with defining generators in this way is that callers must be aware
# that the iterators returned are stateful and cannot be re-used. See the next item, 31,
# for more on this.
