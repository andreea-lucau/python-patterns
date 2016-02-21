"""Sample usage of the Brigde Factory pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods

class LetterWriter(object):

    def __init__(self, writer):
        self.writer = writer

    def write(self):
        self.writer.start()
        self.writer.add("Hi,")
        self.writer.add("How are things?")
        self.writer.add("Regards, Andreea")
        self.writer.end()


class FileLetterWriter(object):

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def start(self):
        self.file = open(self.filename, "w")

    def add(self, line):
        if not self.file:
            return
        self.file.write(line)
        self.file.write("\n")

    def end(self):
        if self.file:
            self.file.close()


class ConsoleLetterWriter(object):

    def __init__(self):
        super(ConsoleLetterWriter, self).__init__()

    def start(self):
        pass

    def add(self, line):
        # pylint: disable=no-self-use
        print line

    def end(self):
        pass


def write_letter_in_file():
    print "Will write letter to file"
    print
    writer = LetterWriter(FileLetterWriter("out.txt"))
    writer.write()


def write_letter_to_console():
    print "Will write letter to console"
    print
    writer = LetterWriter(ConsoleLetterWriter())
    writer.write()


if __name__ == "__main__":
    write_letter_in_file()
    write_letter_to_console()
