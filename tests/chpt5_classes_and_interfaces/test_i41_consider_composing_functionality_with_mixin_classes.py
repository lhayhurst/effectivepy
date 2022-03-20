# a mix-in is a class that defines only small set of additional methods for its children to provide.
# they don't define their own instance attributes, nor require an __init__ constructor call


class ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for k, v in instance_dict.items():
            output[k] = self._traverse(k, v)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, "__dict__"):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):
    __slots__ = ["value", "left", "right"]

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def test_mixin():
    tree = BinaryTree(10, left=BinaryTree(7, right=BinaryTree(9)), right=BinaryTree(13, left=BinaryTree(11)))

    assert tree.to_dict() == {
        "left": {"left": None, "right": {"left": None, "right": None, "value": 9}, "value": 7},
        "right": {"left": {"left": None, "right": None, "value": 11}, "right": None, "value": 13},
        "value": 10,
    }


# One nice thing about mixins is that you can override some of their methods if you don't like how they work.
def test_mixin_with_override():
    class BinaryTreeWithParent(BinaryTree):
        def __init__(self, value, left=None, right=None, parent=None):
            super().__init__(value, left=left, right=right)
            self.parent = parent

        # the addition of parent can create circles in the graph. override _traverse (grossss) to handle
        # this is gross because it tightly couples us!
        def _traverse(self, key, value):
            if isinstance(value, BinaryTreeWithParent) and key == "parent":
                return value.value  # prevent the cycle
            else:
                return super()._traverse(key, value)

    root = BinaryTreeWithParent(10)
    root.left = BinaryTreeWithParent(7, parent=root)
    root.left.right = BinaryTreeWithParent(9, parent=root.left)
    assert root.to_dict() == {
        "left": {
            "left": None,
            "parent": 10,
            "right": {"left": None, "parent": 7, "right": None, "value": 9},
            "value": 7,
        },
        "parent": None,
        "right": None,
        "value": 10,
    }
