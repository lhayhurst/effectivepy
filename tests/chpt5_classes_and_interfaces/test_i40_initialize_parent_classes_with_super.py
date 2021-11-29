def test_old_way():
    class MyBase:
        __slots__ = "value"

        def __init__(self, value):
            self.value = value

    class MyDeriv(MyBase):
        def __init__(self, value):
            MyBase.__init__(self, value)

    md = MyDeriv(3.14)
    assert md.value == 3.14


# but, things can get weird when you have multiple parents, or a diamond inheritance structure. consider:
def test_multiple_parents_inheritance_weirdness():
    class MyBase:
        __slots__ = "value"

        def __init__(self, value):
            self.value = value

    class TimesTwo:
        def __init__(self):
            self.value *= 2

    class PlusFive:
        def __init__(self):
            self.value += 5

    class Weirdness(MyBase, PlusFive, TimesTwo):
        def __init__(self, value):
            MyBase.__init__(self, value)
            TimesTwo.__init__(self)
            PlusFive.__init__(self)

    w = Weirdness(5)
    assert w.value == 15  # not 20, which is what you might expect based on the decl order!


def test_diamond_inheritance_weirdness():
    class B:
        __slots__ = "value"

        def __init__(self, value):
            self.value = value

    class C(B):
        def __init__(self, value):
            B.__init__(self, value)
            self.value *= 7

    class D(B):
        def __init__(self, value):
            B.__init__(self, value)
            self.value += 9

    class E(C, D):
        def __init__(self, value):
            C.__init__(self, value)
            D.__init__(self, value)

    e = E(5)
    assert e.value == 14  # should be (5 * 7) + 9 == 44 but is 14!
    # the call to the second classes constructor actually resets the value, completely
    # ignoring the call to the first constructor.


# to solve these problems, Python has the build in super function that does things like
# ensure ordering is deterministic and that base class constructors only get called one


def test_super():
    class B:
        __slots__ = "value"

        def __init__(self, value):
            self.value = value

    class T7(B):
        def __init__(self, value):
            super().__init__(value)
            self.value *= 7

    class P9(B):
        def __init__(self, value):
            super().__init__(value)
            self.value += 9

    class E(T7, P9):
        def __init__(self, value):
            super().__init__(value)
            super().__init__(value)

    e = E(5)
    assert e.value == 98

    # ok, why 98 and not 44? is it:
    # (5*7) + 9 or
    # 5 * (7 + 9)

    # the answer is the second. the reasons is of the "Standard Method Resolution Order" (MRO)! watch:
    mros = [repr(cls) for cls in E.mro()]
    assert mros == [
        "<class 'chpt5_classes_and_interfaces.test_i40_initialize_parent_classes_with_super.test_super.<locals>.E'>",
        "<class 'chpt5_classes_and_interfaces.test_i40_initialize_parent_classes_with_super.test_super.<locals>.T7'>",
        "<class 'chpt5_classes_and_interfaces.test_i40_initialize_parent_classes_with_super.test_super.<locals>.P9'>",
        "<class 'chpt5_classes_and_interfaces.test_i40_initialize_parent_classes_with_super.test_super.<locals>.B'>",
        "<class 'object'>",
    ]

    # based on this you can see that the ordering is E, then C, then D, than B, as declared. so the call tree is:
    # E constructor called
    # T7 constructor called
    # P6 constructor called
    # Base constructor called, value is set to 5
    # back in the P9 constructor, value is 5 + 9 == 14
    # back to the T7 consructor, when mults 14 * 7 == 9
    # back to E constructor
    # back to test
