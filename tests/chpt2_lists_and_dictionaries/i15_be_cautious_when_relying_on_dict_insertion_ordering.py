# in py 3.5 and earlier, iterating over a dict would return keys in arbitrary order
# as of py 3.7, dictionaries will preserve insertion order


def test_insert_into_dictionary_preserves_insertion_order():
    d = {"cat": "kitten", "dog": "puppy"}
    keys = list(d.keys())
    assert keys == ["cat", "dog"]
    values = list(d.values())
    assert values == ["kitten", "puppy"]


def test_kwargs_preserves_insertion_order():
    def my_func(**kwargs):
        ret = []
        for key, value in kwargs.items():
            ret.append(f"{key}={value}")
        return ret

    a = my_func(goose="gosling", kangaroo="joey")
    assert a == ["goose=gosling", "kangaroo=joey"]


def test_classes_preserve_declaration_order():
    class BabyNames:
        def __init__(self):
            self.alligator = "hatchling"
            self.elephant = "calf"

    a = BabyNames()
    assert list(a.__dict__.items()) == [("alligator", "hatchling"), ("elephant", "calf")]


# don't always assume order is preserved, though
# programmers could be implemeting their own custom container types that implement
# the standard protocols matching list, dict, etc.
