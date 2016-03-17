"""Sample usage of the Iterator pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods

class Europe(object):

    def __init__(self):
        self._est = ["Romania", "Poland", "Ukraine"]
        self._south = ["Greece", "Italy", "Spain"]
        self._west = ["France", "UK", "Ireland"]
        self._north = ["Norway", "Sweeden", "Finland"]

        self._region = self._est
        self._index = -1

    def __iter__(self):
        for country in self._est:
            yield country

        for country in self._south:
            yield country

        for country in self._west:
            yield country

        for country in self._north:
            yield country


    def __call__(self):
        self._index += 1
        if self._index == len(self._region):
            if self._region == self._north:
                raise StopIteration()
            elif self._region == self._est:
                self._region = self._south
                self._index = 0
            elif self._region == self._south:
                self._region = self._west
                self._index = 0
            elif self._region == self._west:
                self._region = self._north
                self._index = 0

        return self._region[self._index]


class Continents(object):

    def __init__(self):
        self._continents = {
            "Europe": ["Romania", "Ireland", "France"],
            "Asia": ["Japan", "China"],
            "Africa": ["Nigeria", "Marocco"],
            "America": ["Peru"],
        }

    def __getitem__(self, index):
        return sorted(self._continents)[index]


def visit_europe():
    print "Iterate using the __iter__"
    europe = Europe()
    for country in europe:
        print "Visinting", country
    print

    print "Iterate using the iter(callable, sentinel)"
    for country in iter(Europe(), "Italy"):
        print "Visinting", country
    print


def visit_the_world():
    print "Iterate with __getitem__"
    for continent in Continents():
        print "Visiting", continent


if __name__ == "__main__":
    visit_europe()
    visit_the_world()
