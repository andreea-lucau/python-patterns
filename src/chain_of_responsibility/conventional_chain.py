"""Sample for the Chain of Responsibility pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods

class Worker(object):
    TYPE = "worker"

    def __init__(self, successor):
        self._successor = successor

    def handle(self, work):
        if work == self.TYPE:
            print self.TYPE, "has work to do"
        elif self._successor:
            self._successor.handle(work)


class Manager(Worker):
    TYPE = "manager"


class Secretary(Worker):
    TYPE = "secretary"


class ProductManager(Worker):
    TYPE = "product manager"


class TeamLead(Worker):
    TYPE = "team lead"


def run_chain():
    tasks = ["manager", "worker", "secretary", "product manager", "team lead"]
    chain = Manager(Worker(Secretary(ProductManager(TeamLead(None)))))

    for task in tasks:
        chain.handle(task)


if __name__ == "__main__":
    run_chain()
