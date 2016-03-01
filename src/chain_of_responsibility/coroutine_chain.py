"""Sample for the Chain of Responsibility pattern."""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods

import functools


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        generator.next()
        return it
    return wrapper


@coroutine
def worker(successor=None):
    while True:
        work = yield
        if work == "worker":
            print "worker has work to do"
        elif successor:
            successor.send(work)


@coroutine
def manager(successor=None):
    while True:
        work = yield
        if work == "manager":
            print "manager has work to do"
        elif successor:
            successor.send(work)


@coroutine
def secretary(successor=None):
    while True:
        work = yield
        if work == "secretary":
            print "secretary has work to do"
        elif successor:
            successor.send(work)


@coroutine
def product_manager(successor=None):
    while True:
        work = yield
        if work == "product manager":
            print "product manager has work to do"
        elif successor:
            successor.send(work)


@coroutine
def team_lead(successor=None):
    while True:
        work = yield
        if work == "team lead":
            print "team lead has work to do"
        elif successor:
            successor.send(work)


def run_chain():
    tasks = ["manager", "worker", "secretary", "product manager", "team lead"]
    chain = manager(worker(secretary(team_lead(product_manager()))))

    #it = chain()
    for task in tasks:
        chain.send(task)


if __name__ == "__main__":
    run_chain()
