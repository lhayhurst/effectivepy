from collections import namedtuple
from dataclasses import dataclass
from typing import List


# Python's built in dictionary and tuple types make it easy to keep track of dynamic state
# but avoid managing internal state if you are doing more than one level of internal nesting
# using dicts inside dicts inside ... makes your code hard to read, and hard to maintain


def test_gross_aka_too_many_levels_of_nested_built_in_types():
    team = {
        "Elanore": {"attempts": 457, "scores": [{"value": -2.5, "time": "42341JB", "reason": "being mean to Chidi"}]},
        "Chidi": {"attempts": 457, "scores": [{"value": 3.14, "time": "42341JB", "reason": "being nice to Elanore"}]},
    }
    assert list(team.keys()) == ["Elanore", "Chidi"]
    assert team["Chidi"]["scores"][0]["time"] == "42341JB"


# when the bookkeeping gets overcomplicated, break it into classes.
# you can then provide well defined interfaces that better encapsulate your data
# this also allows you to create a layer of abstraction between your interface, and your concrete impls.


def test_better():
    @dataclass
    class Score:
        value: float
        time: str
        reason: str

    @dataclass
    class Player:
        scores: List[Score]
        attempts: int

    team = {
        "Elanore": Player(attempts=457, scores=[Score(-2.5, "42341JB", reason="being mean to Chidi")]),
        "Chidi": Player(attempts=457, scores=[Score(4.2, "42341JB", reason="being nice to Elanore")]),
    }

    assert list(team.keys()) == ["Elanore", "Chidi"]
    assert team["Chidi"].scores[0].reason == "being nice to Elanore"


# named tuples have two limitations:
# 1 you don't get default argument values. could be a good thing ;-)
# 2 the attribute values of the namedtuple instance is accessible by the client using
# numerical indexes and enumerations. this can create bad coupling between client and library code.
# if you aren't in control of the client usages, better to use an actual class

Grade = namedtuple("Grade", ("score", "weight"))


def test_demonstrate_named_tuple_issues():
    g = Grade(95, 1.2)
    assert g[0] == 95  # gross
    assert g[1] == 1.2  # gross
    assert list(g) == [95, 1.2]  # gross
