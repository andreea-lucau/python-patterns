"""Sample usage of the Composite pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods
import os

class Item(object):

    def __init__(self, name, *children):
        self.name = name
        self.children = children

    def items(self):
        return iter(self.children)

    def walk(self, indent=None):
        if indent is None:
            indent = ""

        print indent + self.name
        for item in self.items():
            item.walk(indent + "\t")

    @classmethod
    def create_dir(cls, name, children):
        return Item(name, *children)

    @classmethod
    def create_file(cls, name):
        return Item(name)


def traverse_directory(path):
    items = build_structure(path)

    for item in items:
        item.walk()


def build_structure(path):
    items = []

    for name in os.listdir(path):
        # Ignore hidden files/folders
        if name.startswith("."):
            continue
        if os.path.isdir(os.path.join(path, name)):
            children = build_structure(os.path.join(path, name))
            items.append(Item.create_dir(name, children))
        else:
            items.append(Item.create_file(name))

    return items


if __name__ == "__main__":
    traverse_directory("/home/%s" % os.getlogin())
