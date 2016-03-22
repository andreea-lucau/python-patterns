"""Sample usage of the template pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods
import abc

class Letter(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.name = "Tobias"

    def write(self):
        print "%s,\n" % self.get_greeting()
        print self.get_presentation(),
        print self.get_purpose(),
        print self.get_request()

        print "\n%s,\n%s" % (self.get_signature(), self.name)

    @abc.abstractmethod
    def get_greeting(self):
        pass

    @abc.abstractmethod
    def get_presentation(self):
        pass

    @abc.abstractmethod
    def get_purpose(self):
        pass

    @abc.abstractmethod
    def get_request(self):
        pass

    @abc.abstractmethod
    def get_signature(self):
        pass


class EnglishLetter(Letter):

    def get_greeting(self):
        return "Dear Sir"

    def get_presentation(self):
        return "I am your long lost cousin."

    def get_purpose(self):
        return ("I'm writing with the hope that we can "
                "meet next time I am in town.")

    def get_request(self):
        return "Where would be a good place for you?"

    def get_signature(self):
        return "Sincerely yours"


class FrenchLetter(Letter):

    def get_greeting(self):
        return "Cher Monsieur"

    def get_presentation(self):
        return "Je suis votre cousine longtemps perdue."

    def get_purpose(self):
        return ("Je vous ecris avec l'espoir que nous pouvons "
                "rencontrer a la prochaine fois que je suis en ville.")

    def get_request(self):
        return "Ou serait un bon endroit pour vous?"

    def get_signature(self):
        return "Cordialement"


def write_letter():
    EnglishLetter().write()
    print '\n' + '-' * 40 + '\n'
    FrenchLetter().write()


if __name__ == "__main__":
    write_letter()
