def test_simple_sort():
    numbers = [93, 86, 11, 68, 70]
    numbers.sort()  # in place!
    assert numbers == [11, 68, 70, 86, 93]


# but what does sort do for objects?


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name!r}, {self.weight})"


def test_object_sort():
    level = Tool("level", 3.5)
    hammer = Tool("hammer", 1.25)
    screwdriver = Tool("screwdriver", 0.5)
    chisel = Tool("chisel", 0.25)
    tools = [level, hammer, screwdriver, chisel]

    tools.sort(key=lambda t: t.weight)

    assert tools[0] == chisel
    assert tools[1] == screwdriver
    assert tools[2] == hammer
    assert tools[3] == level


def test_can_sort_using_multiple_critera():
    level = Tool("level", 3.5)
    hammer = Tool("hammer", 3.5)
    screwdriver = Tool("screwdriver", 0.5)
    chisel = Tool("chisel", 0.25)

    tools = [screwdriver, hammer, chisel, level]

    tools.sort(key=(lambda t: (t.weight, t.name)), reverse=True)

    assert tools[0] == level
    assert tools[1] == hammer
    assert tools[2] == screwdriver
    assert tools[3] == chisel
