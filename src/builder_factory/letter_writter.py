"""Example of using the BuilderFactory pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,duplicate-code
import abc
import argparse


class LetterBuilder(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.greeting = None
        self.question = None
        self.signature = None

    @abc.abstractmethod
    def add_greeting(self):
        pass

    @abc.abstractmethod
    def add_question(self):
        pass

    @abc.abstractmethod
    def add_signature(self):
        pass

    def write(self):
        print "{greeting},\n\n\t{question}\n\n{signature}".format(
            greeting=self.greeting, question=self.question,
            signature=self.signature)


class EnglishLetterBuilder(LetterBuilder):
    def add_greeting(self):
        self.greeting = "Hello"

    def add_question(self):
        self.question = "How are you?"

    def add_signature(self):
        self.signature = "Love, Andreea"


class RomanianLetterBuilder(LetterBuilder):
    def add_greeting(self):
        self.greeting = "Buna"

    def add_question(self):
        self.question = "Ce mai faci?"

    def add_signature(self):
        self.signature = "Cu drag, Andreea"


def write_letter(language):
    if language == "en":
        builder = EnglishLetterBuilder()
    elif language == "ro":
        builder = RomanianLetterBuilder()

    builder.add_greeting()
    builder.add_question()
    builder.add_signature()

    builder.write()


def parse_args():
    """Parse command line parameters.

    The only accepted parameter is "language".
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("language", metavar="language",
                        choices=["en", "ro"])
    return parser.parse_args()


if __name__ == "__main__":
    write_letter(parse_args().language)
