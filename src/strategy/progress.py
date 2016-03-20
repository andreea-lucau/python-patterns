"""Sample usage of the Strategy pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods

import os
import sys
import termios
import time
import tty

class Progress(object):

    def __init__(self, minimum, maximum, display):
        super(Progress, self).__init__()

        self.minimum = minimum
        self.maximum = maximum
        self.value = 0
        self.display = display

    def reset(self):
        self.value = 0

    def set_display(self, display):
        self.display = display

    def do_work(self):
        for value in [0, 1, 10, 10, 25, 45, 50, 50, 65]:
            self.update_value(value)
            time.sleep(1)

    def update_value(self, value):
        if self.value != value:
            self.value = value
            self.display(int(float(self.value) / self.maximum * 100))


def progress_bar_display(value):
    print "Progress:",
    for _ in range(value):
        print unichr(0x2585),
    print


def progress_percent_display(value):
    print "Progress:", value, "%"


def read_command():
    stdin_fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(stdin_fd)
    try:
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_settings)


def display_progress():
    progress = Progress(0, 100, progress_bar_display)
    progress.do_work()

    print "Press any key to change the display strategy"
    input_command = read_command()

    progress.reset()
    progress.set_display(progress_percent_display)
    progress.do_work()


if __name__ == "__main__":
    display_progress()
