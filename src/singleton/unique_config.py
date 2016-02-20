"""Example of the Singleton pattern for a class."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,duplicate-code
import random

CONFIG_PARAMS_NO = 5
MIN_VALUE = 0
MAX_VALUE = 100


class Singleton(type):
    def __init__(cls, name, bases, attrs):
        super(Singleton, cls).__init__(name, bases, attrs)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class Config(object):
    __metaclass__ = Singleton

    def __init__(self):
        for param_id in range(CONFIG_PARAMS_NO):
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
    for i in range(5):
        config = Config()
        print "Config", i, config
