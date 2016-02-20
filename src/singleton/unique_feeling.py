"""Example of the Singleton pattern for a function."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,duplicate-code
import random

FEELINGS = ["joy", "sadness", "melancholie", "exuberance", "restlessness"]


def get_feeling():
    if not get_feeling.feeling:
        get_feeling.feeling = FEELINGS[random.randint(0, len(FEELINGS) - 1)]

    return get_feeling.feeling

get_feeling.feeling = None


if __name__ == "__main__":
    for _ in range(5):
        print "Checking feeling...", get_feeling()
