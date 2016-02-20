"""Example of the Singleton pattern for a class."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,duplicate-code
from functools import wraps
import random

CONFIG_PARAMS_NO = 5
MIN_VALUE = 0
MAX_VALUE = 100
CONFIGS_NO = 5


def singleton(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in singleton.instances:
            singleton.instances[cls] = cls(*args, **kwargs)
        return singleton.instances[cls]

    return wrapper

singleton.instances = {}


@singleton
class Config(object):
    """Generic configuration"""

    def __init__(self, params_no):
        for param_id in range(params_no):
            self.__dict__["param" + str(param_id)] = "value" + str(
                random.randint(MIN_VALUE, MAX_VALUE))

    def __str__(self):
        result = []
        for param in sorted(self.__dict__):
            if param.startswith("param"):
                value = self.__dict__[param]
                result.append("%s=%s" % (param, value))

        return ",".join(result)

    def get(self, param):
        if param.startswith("param"):
            return self.__dict__.get(param)
        raise KeyError("No such param %s", param)

    def set(self, param, value):
        if param.startswith("param") and param in self.__dict__:
            self.__dict__[param] = value
        raise KeyError("No such attribute %s", param)


if __name__ == "__main__":
    for i in range(CONFIGS_NO):
        config = Config(CONFIG_PARAMS_NO)
        print "Config", i, config
