"""Sample usage of the Flyweight pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods
import argparse
import os
import psutil
import textwrap


class Letter(object):

    def __init__(self, letter):
        self.letter = letter

    def upper(self, try_cache=False):
        if try_cache:
            return Letter.get(self.letter.upper())
        else:
            return Letter(self.letter.upper())

    @classmethod
    def get(cls, letter):
        if letter not in cls.__letters:
            cls.__letters[letter] = Letter(letter)

        return cls.__letters[letter]

    __letters = dict()


class Word(object):

    def __init__(self, word, unique_letters):
        self.unique_letters = unique_letters
        if unique_letters:
            self.letters = [Letter.get(l) for l in word]
        else:
            self.letters = [Letter(l) for l in word]

    def get(self):
        return "".join([l.letter for l in self.letters])

    def upper(self):
        self.letters = [
            l.upper(try_cache=self.unique_letters)
            for l in self.letters
        ]


def print_memory_usage(message):
    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss

    human_readable_memory = memory
    unit = ""
    for index, size in enumerate(("K", "M", "G")):
        new_step = int(memory / pow(1024, index + 1))
        if new_step == 0:
            print message.ljust(15), str(human_readable_memory) + unit
            return
        unit = size
        human_readable_memory = new_step

    print message.ljust(15), str(human_readable_memory) + unit


def write_letter(unique_letters=False):
    text = textwrap.dedent("""\
        In computer programming, flyweight is a software design pattern. A
        flyweight is an object that minimizes memory use by sharing as much
        data as possible with other similar objects; it is a way to use objects
        in large numbers when a simple repeated representation would use an
        unacceptable amount of memory. Often some parts of the object state can
        be shared, and it is common practice to hold them in external data
        structures and pass them to the flyweight objects temporarily when they
        are used.

        A classic example usage of the flyweight pattern is the data structures
        for graphical representation of characters in a word processor. It
        might be desirable to have, for each character in a document, a glyph
        object containing its font outline, font metrics, and other formatting
        data, but this would amount to hundreds or thousands of bytes for each
        character. Instead, for every character there might be a reference to a
        flyweight glyph object shared by every instance of the same character
        in the document; only the position of each character (in the document
        and/or the page) would need to be stored internally.""")

    print_memory_usage("Text definition")
    words = [
        Word(w, unique_letters)
        for w in "\n\n".join([text] * 100).split(" ")
    ]
    print_memory_usage("List build")
    for word in words:
        word.upper()
    print_memory_usage("List mutated")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--unique_letters", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    write_letter(unique_letters=parse_args().unique_letters)
