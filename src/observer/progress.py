"""Sample usage of the Observer pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods

import os
import time


class Observed(object):

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)
        observer.add_data(self)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()


class Progress(Observed):

    def __init__(self, minimum, maximum):
        super(Progress, self).__init__()

        self.minimum = minimum
        self.maximum = maximum
        self.value = 0

    def update_value(self, value):
        if self.value != value:
            self.value = value
            self.notify_observers()


class ProgressBar(object):

    def __init__(self):
        self.data = None

    def add_data(self, data):
        self.data = data

    def update(self):
        print "Progress:",
        for _ in range(int(float(self.data.value) / self.data.maximum * 100)):
            print unichr(0x2585),
        print


class ProgressPercent(object):

    def __init__(self):
        self.data = None

    def add_data(self, data):
        self.data = data

    def update(self):
        print "Progress:", int(float(self.data.value) / self.data.maximum * 100)


def display_progress():
    progress = Progress(0, 100)
    progress.add_observer(ProgressBar())
    progress.add_observer(ProgressPercent())

    for value in [0, 1, 10, 10, 25, 45, 50, 50, 65]:
        os.system("clear")
        progress.update_value(value)
        time.sleep(1)


if __name__ == "__main__":
    display_progress()
