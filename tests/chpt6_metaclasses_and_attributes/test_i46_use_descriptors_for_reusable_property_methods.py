from weakref import WeakKeyDictionary

import pytest


class Homework:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError(f"Grade must be between 0 and 100, got: {value}")
        self._grade = value


def test_simple_homework():
    galileo = Homework()
    galileo.grade = 95
    assert galileo.grade == 95

    with pytest.raises(ValueError, match="must be between"):
        galileo.grade = -1

    with pytest.raises(ValueError, match="must be between"):
        galileo.grade = 101


# now say we want to give the students a grade for an exam, where the exam has multiple
# subjects, each with separate grade


class TediousExam:
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError(f"Grade must be between 0 and 100, got: {value}")

    # for each section of the exam, I need to add a new prpoerty with the check
    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self.writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self.math_grade = value


# this approach isn't general and it is error prone and it is tedious :/

# the better way to to this with a _descriptor protocol_. this lets you define __get__ and __set__ methods that
# do the validation without boilerplate.


class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError(f"Grade must be between 0 and 100, got: {value}")
        self._values[instance] = value


class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


def test_exam_and_grade():
    exam1 = Exam()
    exam1.writing_grade = 82
    exam1.math_grade = 99
    exam1.science_grade = 75

    exam2 = Exam()
    exam2.writing_grade = 80
    exam2.math_grade = 95
    exam2.science_grade = 90

    assert exam1.writing_grade == 82
    assert exam2.writing_grade == 80


# takeaways
# 1 Reuse behavior and validation of @property methods by defining your own descriptor classes
# 2 Use WeakKeyDictionary to ensure your descriptor classes don't leak
