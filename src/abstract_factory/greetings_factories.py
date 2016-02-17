"""This is a sample code that uses the abstract factory pattern."""
#!/usr/bin/env python
# pylint: disable=too-few-public-methods

import argparse


class AbstractGreetingsFactory(object):
    """Abstract factory for greetings.

    It implements two methods: say_hello and say_goodbye, that return Hello and
    Goodbye objects.
    """

    class Hello(object):
        """Abstract class for saying hello.

        The classes that inherit from it have to implement get.
        """
        def get(self):
            """Return the hello message.

            Raises:
                NotImplementedError
            """
            raise NotImplementedError()

    class Goodbye(object):
        """Abstract class for saying goodbye.

        The classes that inherit from it have to implement get.
        """
        def get(self):
            """Return the goodbye message.

            Raises:
                NotImplementedError
            """
            raise NotImplementedError()

    @classmethod
    def say_hello(cls):
        """Create a Hello class."""
        return cls.Hello()

    @classmethod
    def say_goodbye(cls):
        """Create a Goodbye class."""
        return cls.Goodbye()


class EnglishGreetingsFactory(AbstractGreetingsFactory):
    """English Greetings Factory."""

    class Hello(AbstractGreetingsFactory.Hello):
        """Say Hello in English."""

        def get(self):
            """Return the hello message string."""
            return "Hello"

    class Goodbye(AbstractGreetingsFactory.Goodbye):
        """Say Goodbye in English."""

        def get(self):
            """Return the goodbye message string."""
            return "Goodbye"


class RomanianGreetingsFactory(AbstractGreetingsFactory):
    """Romanian Greetings Factory."""

    class Hello(AbstractGreetingsFactory.Hello):
        """Say Hello in Romanian."""

        def get(self):
            """Return the hello message string."""
            return "Bunaaaa"

    class Goodbye(AbstractGreetingsFactory.Goodbye):
        """Say Goodbye in Romanian."""

        def get(self):
            """Return the goodbye message string."""
            return "Papapapapa"


def say_hello_and_goodbye(language):
    """Print language-specifc hello and goodbye messages."""
    if language == "en":
        hello = EnglishGreetingsFactory.say_hello()
        goodbye = EnglishGreetingsFactory.say_goodbye()
    elif language == "ro":
        hello = RomanianGreetingsFactory.say_hello()
        goodbye = RomanianGreetingsFactory.say_goodbye()

    print hello.get()
    print goodbye.get()


def parse_args():
    """Parse command line parameters.

    The only accepted parameter is "language".
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("language", metavar="language", choices=["en", "ro"])
    return parser.parse_args()


if __name__ == "__main__":
    say_hello_and_goodbye(parse_args().language)
