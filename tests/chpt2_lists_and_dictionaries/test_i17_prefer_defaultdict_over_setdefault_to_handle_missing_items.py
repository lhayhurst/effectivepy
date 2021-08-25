from collections import defaultdict
from typing import Optional


def test_set_default():
    visits = {"Japan": {"Tokyo", "Osaka"}, "Mexico": {"Mexico City", "Puerto Vallarta"}}

    visits.setdefault("France", set()).add("Paris")
    assert visits.get("France") == {"Paris"}


def test_visits_using_default_dict():
    class Visits:
        def __init__(self):
            self.data = defaultdict(set)

        def add(self, country, city):
            self.data[country].add(city)

        def get(self, city) -> Optional[set]:
            return self.data.get(city, None)

    visits = Visits()
    visits.add("France", "Paris")
    assert visits.get("France") == {"Paris"}
    visits.add("France", "Nice")
    assert visits.get("France") == {"Nice", "Paris"}

    usa_visits = visits.get("USA")
    assert usa_visits is None
